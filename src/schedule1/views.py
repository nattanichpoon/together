from django.shortcuts import render, get_object_or_404
from django.conf import settings
from projects.models import Project
from .forms import MeetingForm
from django.http import HttpResponseRedirect
from projects.models import Project
from .models import Meeting
from users.models import UserProfile

# Create your views here.
def myschedule(request):
    title = "My Schedule"
    title_align_center = True
    navtab = True
    projects = Project.objects.filter(members__username=request.user.username)
    meetings = Meeting.objects.all()
    mymeetings = []
    for meeting in meetings:
        for project in projects:
            if meeting.project==project:
                mymeetings.append(meeting)


    context = {
    "title": title,
    "title_align_center":title_align_center,
    "navtab":navtab,
    "mymeetings":mymeetings,
    }
    return render(request, "myschedule.html", context)


def schedule_shared(request):
    title = "Shared Schedule"
    title_align_center = True
    navtab = True
    all_meetings = Meeting.objects.all()

    current_project = Project.objects.filter(id=1)
    #users = current_project.members.all()
    #members = []
    #for user in users:
    #    members.append(UserProfile.objects.get(username=user))

    context = {
    "title": title,
    "title_align_center":title_align_center,
    "navtab":navtab,
    "all_meetings": all_meetings,
    "current_project": current_project,
    #"members": members,
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
# 	project = Project.objects.filter(id=1)
# 	members = Project.members.all()
# 	context ={
# 		'project': project,
# 		'members': members
# 	}
# 	return render(request, 'project_detail.html', context)