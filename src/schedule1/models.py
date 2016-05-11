from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Date(models.Model):
	date = models.IntegerField()
	month = models.CharField(max_length=250)
	def __str__(self):
		return self.date

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)

	def __str__(self):
		return self.album_title

	# primary/unique key; each album has one key
	# Red:pk=1

class Song(models.Model):
	album = models.ForeignKey(Album, on_delete=models.CASCADE)

	def __str__(self):
		return self

class Meeting(models.Model):
	project = models.ForeignKey('projects.Project')
	meetingName = models.CharField(max_length=500)
	meetingAgenda = models.CharField(max_length=1000)
	meetingSummary = models.CharField(max_length=1000)
	meetingDate = models.DateField(default=timezone.now)
	CONFIRM = 'CF'
	REJECT = 'RJ'
	PENDING = 'PD'
	STATUS_CHOICES=(
		(CONFIRM,'Confirm'),
		(REJECT,'Reject'),
		(PENDING, 'Pending'))
	meetingStatus=models.CharField(choices=STATUS_CHOICES, max_length=200)
	confirmedCount = models.IntegerField();

	def get_status(self):
		return self.meetingStatus

	def __str__(self):
		return self.meetingName