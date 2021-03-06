from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from users.models import UserProfile
import datetime, json, math, re
from .forms import ProjectForm, EmailForm, TaskForm, TaskFormNew
from projects.models import Project, Task
from ratePeer.models import Rating
from django.core import serializers
from django.utils import timezone
from django.core.mail import send_mail
from django.core.urlresolvers import resolve





# Create your views here.

def myprojects(request):
	title = "My Projects"
	title_align_center = True
	navtab = True

	profile = UserProfile.objects.get(username=request.user)
	projects = Project.objects.filter(members__username=request.user.username).order_by('dueDate')
	today = datetime.datetime.today()


	context = {
	"title": title,
	"title_align_center":title_align_center,
	"navtab":navtab,
	"profile":profile,
	"projects":projects,
	"today":today,
	}
	return render(request, "myprojects.html", context)

def project_productivity(request,pk):
	project = get_object_or_404(Project, pk=pk)

	
	users = project.members.all()
	ratings = Rating.objects.filter(project=project)
	tasks_aw = Task.objects.filter(project=project,taskState=Task.AWAITING)
	tasks_inp = Task.objects.filter(project=project,taskState=Task.IN_PROGRESS)
	tasks = Task.objects.filter(project=project,taskState=Task.COMPLETED)
	members=[]
	date = timezone.now().date()
	#for task graph
	data_task=[]
	array_task=[]
	data_task.append('Task Distribution')
	#for rating graph
	array_rating=[]
	rates=[]
	i=0
	array_task.append(['Member','Tasks'])
	for user in users:
		m=UserProfile.objects.get(username=user)
		members.append(m)
		totaltasklevel=0
		for task in tasks:
			if task.assignee==user:
				totaltasklevel += int(task.difficultyLevel)
		array_task.append([str(m),totaltasklevel])
		thisrating = ratings.filter(user=user).all()
		totalrating = 0 
		if thisrating.count() > 0:
			for rating in thisrating:
				totalrating += rating.total
			rates.append(totalrating/thisrating.count())
		else:
			rates.append(0)

	totaltasks = Task.objects.filter(project=project).count()
	completed = tasks.count()*100
	progress = 0
	if totaltasks > 0:
		progress = completed/totaltasks
	rotate = (progress*360)/100
	if rotate <= 180:
		small = True
	else:
		small = False

	member_list = [ str(t) for t in members ]
	member_list.insert(0,'')
	rates_list = [ float(t) for t in rates ]
	rates_list.insert(0,'Ratings')

	array_rating.append(member_list)
	array_rating.append(rates_list)

	form = EmailForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")

		subject = "Productivity Report: %s"%(project.projectName)
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,form_email]
		current_url = ''.join(['http://127.0.0.1:8000',request.get_full_path()])

		some_html_message = """
		<h2> View report here </h2>
		<p> %s </p>
		""" %(current_url)
	
		send_mail(subject, 
			form_message, 
			from_email, 
			to_email, html_message=some_html_message,
			fail_silently=True)


	context ={
		'project': project,
		'members': members,
		'tasks': tasks,
		'array_task': json.dumps(array_task),
		'array_rating': json.dumps(array_rating),
		'date':date,
		'progress':progress,
		'rotate':rotate,
		'small': small,
		'tasks_inp': tasks_inp,
		'tasks_aw': tasks_aw,
		'form':form

	}
	

	return render(request, 'project_productivity.html', context)
def send_productivity(request):
	form = EmailForm(request.POST or None)
	if form.is_valid():
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")

		subject = "Productivity Report: %s"%(project.projectName)
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,form_email]
		current_url = resolve(request.path_info).url_name


		somestring='this is some string rec'

		somestring = re.sub('send/$', '', somestring)
		some_html_message = """
		<h2> View report here </h2>
		<p> %s </p>
		""" %(current_url)
	
		send_mail(subject, 
			form_message, 
			from_email, 
			to_email, html_message=some_html_message,
			fail_silently=True)
		context ={'form':form,

		}
	return render(request, 'send_productivity.html', context)



def project_detail(request,pk):
	project = get_object_or_404(Project, pk=pk)
	users = project.members.all()
	members=[]
	for user in users:
		members.append(UserProfile.objects.get(username=user))

	allTasks = Task.objects.order_by('-expectedDate').filter(project=project).all()
	tasks_AW = allTasks.filter(taskState=Task.AWAITING, assignee=None).order_by('-difficultyLevel')#high difficulty first
	if tasks_AW.count() > 0:
		if timezone.now().date() >= project.grabBy:
			# if task_.assignee == None:
			autoAssign(tasks_AW, users, pk)
			allTasks = Task.objects.order_by('-expectedDate').filter(project=project).all()

	tasks_CP = allTasks.filter(taskState=Task.COMPLETED)
	if allTasks.count() > 0:
		project.projectProgress = int(tasks_CP.count()/allTasks.count())
		project.save()
	size = users.count()
	allTasks = allTasks.order_by('taskState')

	# if request.method =="POST":
	# 	task = get_object_or_404(Task, pk=taskpk)
	# 	form = TaskForm(request.POST, instance=task)
	# 	if form.is_valid() and form.taskState == Task.AWAITING:
	# 		task = form.save(commit=False)
	# 		form.taskState == Task.IN_PROGRESS
	# 		form.save()
	# 	return redirect('project_detail', pk=project.pk)
	context ={
		'project': project,
		'members': members,
		'tasks': allTasks,
		'size':size
	}

	return render(request, 'project_detail.html', context)

def task_detail(request, pk):
	task = get_object_or_404(Task, pk=pk)
	project = get_object_or_404(Project, pk=task.project.pk)
	form = TaskForm(instance = task)
	today = datetime.datetime.today().date()
	# timeLeft = project.grabBy - today
	# projkey = Project.objects.filter(projectName=task.project).pk

	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			task = form.save(commit=False)			
			task.assignee = request.user
			task.taskState = task.IN_PROGRESS
			form.save()
			return redirect('project_detail', pk = project.pk)
			
	return render(request, 'task_detail.html', {'project':project, 'task': task,'form':form, 'today':today})

def task_update(request, pk):
	task = get_object_or_404(Task, pk=pk)
	project = get_object_or_404(Project, pk=task.project.pk)
	form = TaskForm(instance = task)

	ack = False
	inprog = False
	if task.taskState == Task.IN_PROGRESS:
		inprog = True

	if task.taskState == Task.AWAITING:
		ack = True

	if request.method == "POST":
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			task = form.save(commit=False)
			form.save()
			return redirect('project_detail', pk=project.pk)

	return render(request, 'task_update.html', {'project':project, 'task': task, 'form': form, 'inprog':inprog, 'ack':ack})

def project_new(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			# if project.grabBy "None"
			# find user with lowest score and assign harder tasks first
			# everyone assigned, then assign low priority tasks
			# members = []
			# for member in form.members
			# 	members.append(UserProfile.objects.get(username=user))

			# form.members.append
			project = form.save(commit=False)
			project.save()
			project.members = request.POST.getlist('members')
			return HttpResponseRedirect('http://127.0.0.1:8000/projects/')
	else:
		form = ProjectForm()

	return render(request, "project_new.html", {"form":form})

def task_new(request, pk):
	project = get_object_or_404(Project, pk=pk)
	task = Task(project=project)
	form = TaskFormNew(request.POST)
	# form.fields["assignee"].queryset = project.members.all()
	if request.method == "POST":
		
		# form.fields["assignee"].queryset = project.members.all()
		if form.is_valid():
			task = form.save(commit=False)
			task.project = project
			task.save()
			return redirect('project_detail', pk=project.pk)
	# else:
	# 	form = TaskFormNew()
	return render(request, "task_new.html", {"form":form})

def autoAssign(tasks_AW, users, pk):
	for task in tasks_AW:
		task.assignee = find_lazy_member(users, pk)
		# task.taskState = Task.IN_PROGRESS
		task.save()



def view_member(request, pk):
	profile = get_object_or_404(UserProfile, pk=pk)
	user = profile.username
	projects = Project.objects.filter(members__username=user).all()
	projects_count= projects.count()
	ratings = Rating.objects.filter(user=user).all()

	myTaskCount =0
	awaiting = 0
	inprogress = 0
	completed = 0
	projects_completed=0
	inProgressTasks = []
	awaitingTasks = []
	currentTasks =[]
	state=''
	avgRating=0.0
	avgTask=0.0

	if projects.count() > 0:
		for project in projects:
			if project.completed:
				projects_completed+=1
			allTasks = Task.objects.order_by('-expectedDate').filter(project=project).all()
			
			tasks = allTasks.filter(assignee=user).all()
			# currentTasks= tasks.filter(taskState__in=['AW','IP'])
			if tasks.count() > 0:
				awaiting += tasks.filter(taskState = Task.AWAITING).count()
				inprogress += tasks.filter(taskState = Task.IN_PROGRESS).count()
				completed += tasks.filter(taskState = Task.COMPLETED).count()
				for task in tasks.filter(taskState = Task.IN_PROGRESS):
					inProgressTasks.append(task)
					
				for task in tasks.filter(taskState = Task.AWAITING):
					awaitingTasks.append(task)
				for task in tasks.filter(taskState = Task.COMPLETED):
					avgTask+=task.difficultyLevel

				total = awaiting+inprogress+completed
				currentTasks = awaitingTasks+inProgressTasks
				if completed > 0:
					avgTask = myRoundingFunction(((avgTask/completed)),2)
				
		if ratings.count() > 0:
			for rating in ratings:
				avgRating+=rating.total
			avgRating = myRoundingFunction(((avgRating/ratings.count())*4),2)

		context= {
				'profile': profile,
				'user': user,
				'projects': projects, 'tasks': tasks, 
				'awaiting': awaiting,
				'inprogress': inprogress,
				'completed':completed,
				'inProgressTasks': inProgressTasks, 
				'awaitingTasks':awaitingTasks, 
				'total':total, 
				'projects_count':projects_count,
				'avgRating': avgRating,
				'avgTask': avgTask,
				'projects_completed': projects_completed

			}
	return render(request, "view_member.html", context)

def myRoundingFunction(x, n):
    return math.ceil(x * math.pow(10, n)) / math.pow(10, n)

def find_lazy_member(userList, pk):
	project = Project.objects.get(pk=pk)
	allTasks = Task.objects.filter(project=project).all()
	task_point=[]
	#calculate pts for members
	for member in userList: 
		pt = 0
		for task in allTasks:		
			if task.assignee == member:
				pt += task.difficultyLevel
		pt_member = [pt, member]
		task_point.append(pt_member)
	task_point.sort()
	#return the first user in list
	return task_point[0][1]





