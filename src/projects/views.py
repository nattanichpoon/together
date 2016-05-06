from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from users.models import UserProfile
import datetime, json, math
from .forms import ProjectForm
from projects.models import Project, Task
from ratePeer.models import Rating
from django.core import serializers


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
def project_detail(request,pk):
	project = get_object_or_404(Project, pk=pk)
	members = project.members.all()
	context ={
		'project': project,
		'members': members
	}
	return render(request, 'project_detail.html', context)

def project_productivity(request,pk):
	project = get_object_or_404(Project, pk=pk)
	users = project.members.all()
	ratings = Rating.objects.filter(project=project)
	tasks = Task.objects.filter(project=project,taskState=Task.COMPLETED)
	members=[]
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
		'array_task': json.dumps(array_task),
		'array_rating': json.dumps(array_rating)

	}
	

	return render(request, 'project_productivity.html', context)


def mytasks(request):
	title = "My Projects"
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
	return render(request, "mytasks.html", context)

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


