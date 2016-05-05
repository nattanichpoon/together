from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Rating(models.Model):
	project = models.ForeignKey('projects.Project')
	user = models.ForeignKey('auth.User')
	a = 1
	b = 2
	c = 3
	d = 4
	e = 5
	RATINGS = ((e, '5'),(d, '4'),(c, '3'),(b, '2'),(a, '1'))
	rating1 = models.IntegerField(choices=RATINGS, default=e)
	rating2 = models.IntegerField(choices=RATINGS, default=e, max_length=200)
	rating3 = models.IntegerField(choices=RATINGS, default=e, max_length=200)
	rating4 = models.IntegerField(choices=RATINGS, default=e, max_length=200)
	rating5 = models.IntegerField(choices=RATINGS, default=e, max_length=200)
	total = models.IntegerField(default=0, max_length=200)

	def save(self, *args, **kwargs):
		if not self.total:
			self.total = self.rating1 + self.rating2 +self.rating3 + self.rating4+self.rating5
		return super(Rating, self).save(*args, **kwargs)

