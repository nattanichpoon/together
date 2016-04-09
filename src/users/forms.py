from django import forms
from .models import SignUp
from django.contrib.auth.models import User
from registration.forms import RegistrationForm

# class RegistrationForm(RegistrationForm):
# 	class Meta:
# 		model = UserProfile
# 		fields = ['username','first_name','last_name', 'email']
# 	def clean_email(self):
# 		email = self.cleaned_data.get('email')
# 		email_base, provider = email.split("@")
# 		domain, extension = provider.split('.')
# 		return email

# 	def save(self, commit=True):
# 		if not commit:
# 			raise NotImplementedError("Can't create User and UserProfile without database save")
# 		print "Saving..."
# 		user = super(RegistrationForm, self).save(commit=False)
# 		user.username = self.cleaned_data["username"]
# 		user.email = self.cleaned_data["email"]
# 		user.first_name = self.cleaned_data["first_name"]
# 		user.last_name = self.cleaned_data["last_name"]

# 		user_profile = UserProfile(user=user, username=self.cleaned_date['username'],email=self.cleaned_data['email'],first_name=self.cleaned_data['first_name'],last_name=self.cleaned_data['last_name'])
# 		user_profile.save()
# 		print "Saving complete"
# 		return user, user_profile

# class UserForm(forms.ModelForm):
#     password = forms.CharField(min_length=6,label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password','required':'true','class':"form-control"}))
#     username = forms.CharField(label='', min_length=6,
#                     widget=forms.TextInput(attrs={'placeholder': 'Username','required':'true','class':"form-control",'autofocus':'true'}))
#     email = forms.CharField(label='', 
#                     widget=forms.TextInput(attrs={'placeholder': 'Email','required':'true','class':"form-control"}))

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')

# class UserProfileForm(forms.ModelForm):
#     about_me = forms.CharField(label='', 
#                     widget=forms.Textarea(attrs={'placeholder': 'Sobre mi','required':'true','class':"form-control"}))
#     first_name = forms.CharField(label='', 
#                     widget=forms.TextInput(attrs={'placeholder': 'Nombre','required':'true','class':"form-control"}))
#     last_name = forms.CharField(label='', 
#                     widget=forms.TextInput(attrs={'placeholder': 'Apellidos','required':'true','class':"form-control"}))
#     experience = forms.CharField(label='', 
#                     widget=forms.TextInput(attrs={'placeholder': 'Experiencia','required':'true','class':"form-control"}))
#     offers = forms.CharField(label='', 
#                     widget=forms.Textarea(attrs={'placeholder': 'Mensaje','required':'true','class':"form-control"}))

#     class Meta:
#         model = UserProfile
#         fields =('first_name','last_name','about_me','experience','offers')






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

