from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from users.models import UserProfile
import datetime, json, math
from .forms import ProjectForm
from projects.models import Project, Task
from ratePeer.models import Rating
from django.core import serializers
from django.utils import timezone



# Create your views here.

def myprojects(request):
	title = "My lalala"
	title_align_center = True
	navtab = True

	profile = UserProfile.objects.get(username=request.user)
	projects = Project.objects.filter(members__username=request.user.username)
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
	progress = int(project.projectProgress)
	rotate = (progress*360)/100
	if rotate <= 180:
		small = True
	else:
		small = False
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
		for task in tasks:
			if task.assignee==user:
				array_task.append([str(m),int(task.difficultyLevel)])
		for rating in ratings:
			if rating.user==user:
				rates.append(rating.total)


	member_list = [ str(t) for t in members ]
	member_list.insert(0,'')
	rates_list = [ float(t) for t in rates ]
	rates_list.insert(0,'Ratings')

	array_rating.append(member_list)
	array_rating.append(rates_list)
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
		'tasks_aw': tasks_aw

	}
	

	return render(request, 'project_productivity.html', context)


def project_detail(request,pk):
	project = get_object_or_404(Project, pk=pk)
	users = project.members.all()
	members=[]
	for user in users:
		members.append(UserProfile.objects.get(username=user))

	allTasks = Task.objects.order_by('-expectedDate').filter(project=project).all()

	context ={
		'project': project,
		'members': members,
		'tasks': allTasks,
	}

	return render(request, 'project_detail.html', context)

def task_detail(request, pk):
	task = get_object_or_404(Task, pk=pk)
	return render(request, 'task_detail.html', {'task': task})

def project_new(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.save()
			project.members = request.POST.getlist('members')
			return render(request, "project_new.html", '')
	else:
		form = ProjectForm()


		
	return render(request, "project_new.html", {"form":form})

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
		for rating in ratings:
			avgRating+=rating.total
		for project in projects:
			if project.completed:
				projects_completed+=1
			allTasks = Task.objects.order_by('-expectedDate').filter(project=project).all()
			tasks = allTasks.filter(assignee=user).all()
			# currentTasks= tasks.filter(taskState__in=['AW','IP'])

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
		avgRating = myRoundingFunction(((avgRating/ratings.count())*4),2)
		avgTask = myRoundingFunction(((avgTask/completed)),2)
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



