from django.shortcuts import render, get_object_or_404
from django.conf import settings
from projects.models import Project


# Create your views here.
def myschedule(request):
    title = "My Schedule"
    title_align_center = True
    navtab = True

    context = {
    "title": title,
    "title_align_center":title_align_center,
    "navtab":navtab,
    }
    return render(request, "myschedule.html", context)


def schedule_shared(request):
    title = "Shared Schedule"
    title_align_center = True
    navtab = True

    context = {
    "title": title,
    "title_align_center":title_align_center,
    "navtab":navtab,
    }
    return render(request, "schedule_shared.html", context)



#def project_detail(request,pk):
#	project = get_object_or_404(Project, pk=pk)
#	members = project.members.all()
#	context ={
#		'project': project,
#		'members': members
#	}
#	return render(request, 'project_detail.html', context)