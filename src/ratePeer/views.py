from django.shortcuts import render, get_object_or_404, redirect
from .forms import RatingForm
from .models import Rating
from projects.models import Project
from users.models import UserProfile
import math



# Create your views here.
def ratepeer(request,pk):
	myproject = Project.objects.get(pk=pk)
	members= myproject.members.all()
	if request.method == "POST":
		form = RatingForm(request.POST)
		if form.is_valid():
			rating = form.save(commit=False)
			rating.project = myproject
			rating.save()
			
			return render(request, "ratepeer.html", {"project":myproject})
	else:
		form = RatingForm(instance=myproject)

	return render(request, "ratepeer.html", {"form":form, "project":myproject, "members": members})


def myRoundingFunction(x, n):
    return math.ceil(x * math.pow(10, n)) / math.pow(10, n)


def myratings(request):
	ratings = Rating.objects.filter(user=request.user).all()
	rating1 = 0.0
	rating2 = 0.0
	rating3 = 0.0
	rating4 = 0.0
	rating5 = 0.0

	for rating in ratings:
		rating1 += rating.rating1
		rating2 += rating.rating2
		rating3 += rating.rating3
		rating4 += rating.rating4
		rating5 += rating.rating5

	rating1 = (rating1/ratings.count())*20
	rating2 = (rating2/ratings.count())*20
	rating3 = (rating3/ratings.count())*20
	rating4 = (rating4/ratings.count())*20
	rating5 = (rating5/ratings.count())*20

	context = {
		'ratings': ratings,
		'rating1': myRoundingFunction(rating1,2),
		'rating2': myRoundingFunction(rating2,2),
		'rating3': myRoundingFunction(rating3,2),
		'rating4': myRoundingFunction(rating4,2),
		'rating5': myRoundingFunction(rating5,2),
	}
	return render(request, "myratings.html", context)





