from django.shortcuts import render
from .forms import PostForm
 
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

def post_new(request):
    form = PostForm()
    return render(request, 'discussion/post_edit.html', {'form': form})

def post_list(request):
    return render(request, 'discussion/post_list.html', {})