from django import forms

from .models import Rating

class RatingForm(forms.ModelForm):

    class Meta:
        model = Rating
        fields = ('user','rating1', 'rating2', 'rating3', 'rating4','rating5')