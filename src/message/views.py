from django.shortcuts import render
from django.contrib import messages

# Create your views here.
def messages(request):
	title = "My Messages"
	title_align_center = True
	navtab = True

	context = {
	"title": title,
	"title_align_center":title_align_center,
	"navtab":navtab,
	}
	return render(request, "django_messages/inbox.html", context)
