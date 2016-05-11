from django import forms

from .models import Meeting

# when you create a new meeting
class MeetingForm(forms.ModelForm):

	class Meta:
		model = Meeting
		fields = ('project','meetingName','meetingDate','meetingAgenda')

# add summary when the meeting is done
#class SummaryForm(forms.ModelForm):
#
#	class Meta:
#		model = Meeting
#		fields = ('meetingSummary')