from django.contrib import admin

# Register your models here.
#from someotherapp.models import someothermodel
from .forms import SignUpForm, ContactForm
from .models import SignUp #.models -- folder inside 'users' app

class SignUpAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp","updated"]
	form = SignUpForm
	# class Meta:
	# 	model = SignUp

admin.site.register(SignUp, SignUpAdmin)
