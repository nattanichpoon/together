from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group
from decimal import Decimal

# Create your models here.
class Project(models.Model):
	projectName = models.CharField(max_length=200, unique=True,default='Untitled Project')
	members = models.ManyToManyField(User)
	projectProgress = models.DecimalField(default=Decimal('0.00'),max_digits=5,decimal_places=2)
	dueDate = models.DateField(default=timezone.now,blank=True)
	completed = models.BooleanField(default=False)
	

	def get_members(self):
	        return ",".join([str(p) for p in self.members.all()])

	def __str__(self):
		return self.projectName
	

class Task(models.Model):
	project = models.ForeignKey('projects.Project')
	taskName = models.CharField(max_length=200)

	assignee = models.ForeignKey(User, null=True)

	AWAITING = 'AW'
	IN_PROGRESS = 'IP'
	COMPLETED = 'CP'
	STATE = (
		(AWAITING,'Awaiting'),
 		(IN_PROGRESS,'In Progress'),
 		(COMPLETED,'Completed')
	)
	EASY = 1
	MEDIUM = 3
	DIFFICULT = 5
	DIFFICULTY_STATE = ((EASY, 'Easy'), (MEDIUM, 'Medium'), (DIFFICULT, 'Difficult'))

	taskState = models.CharField(choices=STATE, default=AWAITING, max_length=200)
	
	difficultyLevel =models.IntegerField(choices=DIFFICULTY_STATE, default=EASY, max_length=200)
	expectedDate = models.DateField(default=timezone.now,blank=True)
	actualDate = models.DateField(default=timezone.now,blank=True)
	description = models.CharField(blank = True, max_length = 200)
	
	def __str__(self):
		return self.taskName