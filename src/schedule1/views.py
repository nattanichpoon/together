from django.shortcuts import render, get_object_or_404
from django.conf import settings
from projects.models import Project
from .forms import MeetingForm
from django.http import HttpResponseRedirect
from projects.models import Project
from users.models import UserProfile
from .models import Meeting

# Create your views here.
def myschedule(request):
    title = "My Schedule"
    title_align_center = True
    navtab = True

    profile = UserProfile.objects.get(username=request.user)
    meetings = Meeting.objects.all()
    meeting1 = Meeting.objects.filter(id=1)
    #projects = Project.objects.filter(members__username=request.user.username)
    projects = Project.objects.all()

    context = {
    "title": title,
    "title_align_center":title_align_center,
    "navtab":navtab,
    "profile":profile,
    "meetings":meetings,
    "meeting1":meeting1,
    "projects":projects,

    }
    return render(request, "schedule_shared.html", context)


def schedule_shared(request):
    title = "Shared Schedule"
    title_align_center = True
    navtab = True

    meetings = Meeting.objects.all()
    meeting1 = Meeting.objects.filter(id=1)

    context = {
    "title": title,
    "title_align_center":title_align_center,
    "navtab":navtab,
    'meetings':meetings,
    "meeting1":meeting1,
    }
    return render(request, "schedule_shared.html", context)

def schedule_detail(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    title = "Meeting Detail"
    title_align_center = True
    navtab = True

    #meeting = get_object_or_404(Meeting, pk=pk)
    meetings = Meeting.objects.all()


    context = {
        "title": title,
        "title_align_center": title_align_center,
        "navtab": navtab,
        "meetings":meetings,
        "meeting":meeting,
    }
    return render(request, "meeting_detail.html", context)

def schedule_new(request):
    form = MeetingForm(request.POST)
    if request.method == "POST":
        
        if form.is_valid():
            # if project.grabBy "None"
            # find user with lowest score and assign harder tasks first
            # everyone assigned, then assign low priority tasks
            meeting = form.save(commit=False)
            meeting.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/schedule/')
    # else:
    #     form = MeetingForm()

    return render(request, "meeting_new.html", {"form": form})


# def project_detail(request,pk):
#   project = get_object_or_404(Project, pk=pk)
#   members = project.members.all()
#   context ={
#       'project': project,
#       'members': members
#   }
#   return render(request, 'project_detail.html', context)