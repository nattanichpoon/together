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
	username = models.ForeignKey('auth.User', primary_key=True)
	full_name = models.CharField(max_length=200)
	
	# def save(self):
	# 	# full_name = first_name + " " + last_name
	# 	self.save()
	def __str__(self):
		return self.full_name