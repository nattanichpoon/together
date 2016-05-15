from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Meeting(models.Model):
	project = models.ForeignKey('projects.Project')
	meetingName = models.CharField(max_length=500)
	meetingAgenda = models.CharField(max_length=1000)
	meetingSummary = models.CharField(max_length=1000, blank=True)
	meetingDate = models.DateField(default=timezone.now)
	meetingTime = models.TimeField(default=timezone.now)
	CONFIRM = 'CF'
	REJECT = 'RJ'
	PENDING = 'PD'
	STATUS_CHOICES=(
		(CONFIRM,'Confirm'),
		(REJECT,'Reject'),
		(PENDING, 'Pending'))
	meetingStatus=models.CharField(choices=STATUS_CHOICES, max_length=200, default=PENDING);
	confirmedCount = models.IntegerField(default=0);

	def get_status(self):
		return self.meetingStatus

	def get_confirmedCount(self):
		return self.confirmedCount

	def __str__(self):
		return self.meetingName