from django.shortcuts import render
 
def discussions(request):
	title = "Discussions"
	title_align_center = True
	navtab = True

	context = {
	"title": title,
	"title_align_center":title_align_center,
	"navtab":navtab,
	}
	return render(request, "discussion_home.html", context)
