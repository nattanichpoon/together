from django.shortcuts import render, get_object_or_404
from django.conf import settings
from projects.models import Project
from .forms import MeetingForm
from django.http import HttpResponseRedirect
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

#def schedule_new(request):
#    title = "New Meeting"
#    title_align_center = True
#    navtab = True
#
#    context = {
#        "title": title,
#        "title_align_center": title_align_center,
#        "navtab": navtab,
#    }
#    return render(request, "meeting_new.html", context)

def schedule_new(request):
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            # if project.grabBy "None"
            # find user with lowest score and assign harder tasks first
            # everyone assigned, then assign low priority tasks
            meeting = form.save(commit=False)
            meeting.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/schedule/')
    else:
        form = MeetingForm()

    return render(request, "meeting_new.html", {"form": form})

# def project_detail(request,pk):
# 	project = get_object_or_404(Project, pk=pk)
# 	members = project.members.all()
# 	context ={
# 		'project': project,
# 		'members': members
# 	}
# 	return render(request, 'project_detail.html', context)