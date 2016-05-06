from django.conf import settings
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, ContactForm, UserProfileForm
from django.http import HttpResponseRedirect
from .models import UserProfile
from projects.models import Project, Task
from django.utils import timezone
from ratePeer.models import Rating
import math


# Create your views here.
def home(request):
	title = "Welcome"
	if request.user.is_authenticated():
		try:
			profile = UserProfile.objects.get(username=request.user)
			# return render(request, "myprofile.html", {'profile':profile})
			# return render(request,"test.html",'')
			return HttpResponseRedirect("http://127.0.0.1:8000/profile/")
		except ObjectDoesNotExist:
			print "nothing"
			# form = UserProfileForm()
			# return render(request, "editprofile.html",{'form':form})
	return render(request, "home.html", '')


def about(request):
	context ={
		"title": "About Us"
	}
	return render(request, "about.html", context)

def myRoundingFunction(x, n):
    return math.ceil(x * math.pow(10, n)) / math.pow(10, n)

def myprofile(request):
	awaiting = 0
	inprogress = 0
	completed = 0
	projects_completed=0
	inProgressTasks = []
	awaitingTasks = []
	currentTasks =[]
	i=0
	state=''
	avgRating=0.0
<<<<<<< HEAD
	avgTask=0.0
=======
>>>>>>> nice-from-p
	try:
		profile = UserProfile.objects.get(username=request.user)
		projects = Project.objects.filter(members__username=request.user.username).all()
		projects_count= projects.count()
		date = timezone.now().date()
		ratings = Rating.objects.filter(user=request.user).all()
<<<<<<< HEAD
		myTaskCount =0
=======

>>>>>>> nice-from-p

		if projects.count() > 0:
			for rating in ratings:
				avgRating+=rating.total
			for project in projects:
				if project.completed:
					projects_completed+=1
				allTasks = Task.objects.order_by('-expectedDate').filter(project=project).all()
				tasks = allTasks.filter(assignee=request.user).all()
				# currentTasks= tasks.filter(taskState__in=['AW','IP'])

				awaiting += tasks.filter(taskState = Task.AWAITING).count()
				inprogress += tasks.filter(taskState = Task.IN_PROGRESS).count()
				completed += tasks.filter(taskState = Task.COMPLETED).count()
				for task in tasks.filter(taskState = Task.IN_PROGRESS):
					inProgressTasks.append(task)
					
				for task in tasks.filter(taskState = Task.AWAITING):
					awaitingTasks.append(task)
				for task in tasks.filter(taskState = Task.COMPLETED):
					avgTask+=task.difficultyLevel

			total = awaiting+inprogress+completed
			currentTasks = awaitingTasks+inProgressTasks
			avgRating = myRoundingFunction(((avgRating/ratings.count())*4),2)
<<<<<<< HEAD
			avgTask = myRoundingFunction(((avgTask/completed)),2)
=======

>>>>>>> nice-from-p
		context={
			'currentTasks':currentTasks, 
			'date':date, 
			'profile': profile, 
			'projects': projects, 'tasks': tasks, 
			'awaiting': awaiting,
			'inprogress': inprogress,
			'completed':completed,
			'inProgressTasks': inProgressTasks, 
			'awaitingTasks':awaitingTasks, 
			'total':total, 
			'projects_count':projects_count,
<<<<<<< HEAD
			'avgRating': avgRating,
			'avgTask': avgTask,
			'projects_completed': projects_completed
=======
			'avgRating': avgRating
>>>>>>> nice-from-p
		}


		
		return render(request, "myprofile.html", context)

	except ObjectDoesNotExist:
		print "nothing"

	return render(request, "myprofile.html", '')

def editprofile(request):
	if request.method == "POST":
		form = UserProfileForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = request.user
			user.save()
			return redirect('home')
	else:
		form = UserProfileForm()
		try:
			profile = UserProfile.objects.get(username=request.user)
			return render(request,'editprofile.html',{ 'form': form, 'profile': profile})
		except ObjectDoesNotExist:
			print "nothing"
	return render(request,'editprofile.html',{ 'form': form})

	
def contact(request):
	title = "Have feedback? Leave us a message!"
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.iteritems():
		# 	print key, value
			#print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")

		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email,'nattanichpoon@gmail.com']
		contact_message = "%s: %s via %s"%(
			form_full_name, 
			form_message, 
			form_email)
		some_html_message = """
		<h2> %s </h2>
		<h3> - %s  </h3>
		<p> %s </p>
		""" %(form_message,form_full_name, form_email)
	
		send_mail(subject, 
			contact_message, 
			from_email, 
			to_email, html_message=some_html_message,
			fail_silently=True)

	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,

	}
	return render(request, "contact.html", context)