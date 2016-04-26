from django.shortcuts import render
from django.conf import settings
<<<<<<< HEAD
from users.models import UserProfile
from projects.models import Project
import datetime

=======
from .forms import ProjectForm
from users.models import UserProfile
from projects.models import Project, Task
>>>>>>> p

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

<<<<<<< HEAD
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
=======
def project_new(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			project.save()
			project.members = request.POST.getlist('members')
			return render(request, "project_new.html", '')
	else:
		form = ProjectForm(request.GET)


		
	return render(request, "project_new.html", {"form":form})
>>>>>>> p
