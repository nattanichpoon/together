from django.shortcuts import render
from django.contrib import messages
from users.models import UserProfile
# Create your views here.
def messages(request):
	title = "My Messages"
	title_align_center = True
	navtab = True
	profile = UserProfile.objects.get(username=request.user)

	context = {
	"title": title,
	"title_align_center":title_align_center,
	"navtab":navtab,
	"profile":profile,

	}
	return render(request, "django_messages/inbox.html", context)
