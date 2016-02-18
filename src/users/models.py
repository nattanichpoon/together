from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered



# Create your models here.
class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120,blank=True, null=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)

	def __unicode__(self): #python 3 __str__
		return self.email #dispayed in signup field in admin page


class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	full_name = models.CharField(max_length=120,blank=True, null=True)

	def __unicode__(self): #python 3 __str__
		return self.user #dispayed in signup field in admin page

	def user_registered_callback(sender, user, request, **kwargs):
	    profile = UserProfile(user=user)
	    profile.full_name = request.POST["full_name"]
	    profile.save()
 	
 	user_registered.connect(user_registered_callback)


# class Contact(models.Model):
# 	email = models.EmailField()
# 	full_name = models.CharField(max_length=120,blank=True, null=True)
# 	message = models.TextField()
# 	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

# 	def __unicode__(self): #python 3 __str__
# 		return self.email #dispayed in signup field in admin page