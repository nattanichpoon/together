from django import forms
from .models import SignUp, UserProfile
from django.contrib.auth.models import User
from registration.forms import RegistrationForm

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('full_name','avatar')
	def __init__(self, *args, **kwargs): 
		super(UserProfileForm, self).__init__(*args, **kwargs)
		self.fields['avatar'].label = 'Gender'
	



class ContactForm(forms.Form):

	full_name = forms.CharField(required=False)
	email = forms.EmailField()
	message = forms.CharField()

class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		return full_name

