from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from users.models import UserProfile
import datetime
from .forms import ProjectForm
from projects.models import Project, Task

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
	members = project.get_members()


	context ={
		'project': project,
		'members': members
	}
	

	return render(request, 'project_detail.html', context)

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
