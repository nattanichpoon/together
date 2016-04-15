from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# # Create your models here.
# class Project(models.Model):
# 	# projectID = models.IntegerField(primary_key=True)
# 	projectName = models.CharField(max_length=200,null=True)
# 	teamMembers = models.ManyToManyField('auth.User')
# 	# projectTasks = models.ForeignKey('project.Task', on_delete=models.CASCADE)
# 	projectProgress = models.DecimalField(decimal_places = 2, max_digits = 5)
#  # discussion = models.ForeignKey('discussion.Post', on_delete=models.CASCADE)
#  	def __str__(self):
#  		return self.projectName

# # class Task(models.Model):
# # 	taskName = models.CharField(max_length=200)
# # 	AWAITING = 'AW'
# # 	IN_PROGRESS = 'IP'
# # 	COMPLETED = 'CP'
# # 	STATE = (
# # 		(AWAITING,'awaiting'),
# #  		(IN_PROGRESS,'In Progress'),
# #  		(COMPLETED,'Completed')
# # 	)
# # 	EASY = 'E'
# # 	MEDIUM = 'M'
# # 	DIFFICULT = 'D'
# # 	DIFFICULTY_STATE = ((EASY, 'Easy'), (MEDIUM, 'Medium'), (DIFFICULT, 'Difficult'))

# # 	# taskID = models.IntegerField(primary_key=True)
# # 	projectID = models.ForeignKey('project.Project', related_name='tasks', null=True)
# # 	taskState = models.CharField(choices=STATE, default=AWAITING, max_length=200)
# # 	taskCompletion = models.BooleanField(default=False)
# #  #assignee = 
	
# # 	difficultyLevel =models.CharField(choices=DIFFICULTY_STATE, default=EASY, max_length=200) #choices = easy, intermediate, hard? 
# # 	expectedDate = models.DateField(default=timezone.now,blank=True)
# # 	actualDate = models.DateField(default=timezone.now,blank=True)
# # 	# daysLeft = models.DateField() #countdown
# # 	def __str__(self):
# # 		return self.taskName