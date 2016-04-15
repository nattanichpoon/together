from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Project(models.Model):
	projectID = models.IntegerField(primary_key = True)
	projectName = models.CharField(max_length = 200)
	teamMembers = models.ManyToManyField('auth.User', related_name = 'my_projects')
	# projectTasks = models.ForeignKey('project.Task', on_delete=models.CASCADE)
	projectProgress = models.DecimalField(decimal_places = 2, max_digits = 5)
 # discussion = models.ForeignKey('discussion.Post', on_delete=models.CASCADE)

class Task(models.Model):
	AWAITING = 'AW'
	IN_PROGRESS = 'IP'
	COMPLETED = 'CP'
	STATE = (
		(AWAITING,'awaiting'),
 		(IN_PROGRESS,'In Progress'),
 		(COMPLETED,'Completed')
	)

	taskID = models.IntegerField(primary_key = True)
	projectID = models.ForeignKey('project.Project')
	taskState = models.CharField(choices = STATE, default = AWAITING, max_length = 200)
	taskCompletion = models.BooleanField(default = False)
 #assignee = 
	difficultyLevel = models.CharField(max_length = 30) #choices = easy, intermediate, hard? 
	expectedDate = models.DateField()
	actualDate = models.DateField()
	daysLeft = models.DateField() #countdown