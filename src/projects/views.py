from django.shortcuts import render
from django.conf import settings
from .forms import ProjectForm
from users.models import UserProfile
from projects.models import Project, Task

# Create your views here.
def myprojects(request):
	title = "My lalala"
	title_align_center = True
	navtab = True

	context = {
	"title": title,
	"title_align_center":title_align_center,
	"navtab":navtab,
	}
	return render(request, "myprojects.html", context)

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
