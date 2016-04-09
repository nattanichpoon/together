from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):
	title = "Welcome"
	if request.user.is_authenticated():
		return render(request, "myprofile.html", '')
	return render(request, "home.html", '')


def about(request):
	context ={
		"title": "About Us"
	}
	return render(request, "about.html", context)

def myprofile(request):
	return render(request, "myprofile.html", '')

def editprofile(request):
	try:
		profile = request.user.userprofile
	except UserProfile.DoesNotExist:
		profile = UserProfile(user=request.user)
	if request.method == 'POST':
		form = UserProfileForm(data=request.POST, instance=profile)
		if form.is_valid():
			form.save()
			# return HttpResponse("Exito!")
		else:
			form = UserProfileForm(instance=profile)
	else:
		form = UserProfileForm()

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