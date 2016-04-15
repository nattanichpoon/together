from django.shortcuts import render
from django.conf import settings


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
