from django import forms

from .models import Rating
from projects.models import Project
from users.models import UserProfile
from django.contrib.auth.models import User


class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('user','rating1', 'rating2', 'rating3', 'rating4','rating5')

    def __init__(self, *args, **kwargs): 
		super(RatingForm, self).__init__(*args, **kwargs)
		self.fields['rating1'].label = 'Attends group meetings regularly and arrives on time.'
		self.fields['rating2'].label = 'Contributes meaningfully to group discussions.'
		self.fields['rating3'].label = 'Prepares work in a quality manner.'
		self.fields['rating4'].label = 'Demonstrates a cooperative and supportive attitude.'
		self.fields['rating5'].label = 'Contributes significantly to the success of the project.'
