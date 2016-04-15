from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .forms import PostForm, CommentForm
from .models import Post
from users.models import UserProfile

 
def discussions(request):
	title = "Discussions"
	title_align_center = True
	navtab = True
	profile = UserProfile.objects.get(username=request.user)

	context = {
	"title": title,
	"title_align_center":title_align_center,
	"navtab":navtab,
	"profile":profile,

	}
	return render(request, "discussion_home.html", context)

def post_new(request):
    form = PostForm()
    profile = UserProfile.objects.get(username=request.user)
    return render(request, 'post_edit.html', {'form': form,'profile':profile})

def post_list(request):
	# Post.objects.order_by('-created_date')
	# posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date') 
	posts = Post.objects.order_by('-published_date') 
	profile = UserProfile.objects.get(username=request.user)

	return render(request, 'post_list.html', {'posts': posts,'profile':profile})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments = post.comments.order_by('-created_date')
	return render(request, 'post_detail.html', {'post': post, 'comments':comments})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)

	else:
		form = PostForm()
	return render(request, 'post_edit.html', {'form': form})

def add_comment_to_post(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.author = request.user
			comment.post = post
			comment.save()
			return redirect('discussion.views.post_detail', pk=post.pk)
	else:
		form = CommentForm()
	return render(request, 'add_comment_to_post.html', {'form': form})