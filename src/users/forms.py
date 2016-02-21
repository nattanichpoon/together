from registration.forms import RegistrationForm
from django import forms
from .models import SignUp, UserProfile
from django.contrib.auth.models import User

class RegistrationForm(RegistrationForm):
	class Meta:
		model = UserProfile
		fields = ['full_name', 'email']
	def clean_email(self):
		email = self.cleaned_data.get('email')
		email_base, provider = email.split("@")
		domain, extension = provider.split('.')
		return email

	def clean_full_name(self):
		full_name = self.cleaned_data.get('full_name')
		#write validation code.
		return full_name

# class EditProfile(forms.ModelForm):
# 	username = forms.CharField(required=True)
# 	email = forms.EmailField(required=True)
# 	first_name = forms.CharField(required=False)
# 	last_name = forms.CharField(required=False)

# 	class Meta:
# 		model = User
# 		fields = ('username', 'email', 'first_name', 'last_name')

# 	def clean_email(self):
# 		username = self.cleaned_data.get('username')
# 		email = self.cleaned_data.get('email')

# 		if email and User.objects.filter(email=email).exclude(username=username).count():
# 		    raise forms.ValidationError('This email address is already in use. Please supply a different email address.')
# 		return email

# 	def save(self, commit=True):
# 		user = super(RegistrationForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']

# 		if commit:
# 			user.save()

# 		return user


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
		#write validation code.
		return full_name

