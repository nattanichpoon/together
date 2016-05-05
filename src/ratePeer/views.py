from django.shortcuts import render
from .forms import RatingForm
from .models import Rating


# Create your views here.
def ratepeer(request):
	if request.method == "POST":
		form = RatingForm(request.POST)
		if form.is_valid():
			rating = form.save(commit=False)
			rating.save()
			return render(request, "ratepeer.html", '')
	else:
		form = RatingForm()
	
	return render(request, "ratepeer.html", {"form":form})

def myratings(request):
	
	
	return render(request, "myratings.html", '')