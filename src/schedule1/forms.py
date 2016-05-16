from django import forms

from .models import Meeting

# when you create a new meeting
class MeetingForm(forms.ModelForm):

	class Meta:
		model = Meeting
		fields = ('project','meetingName','meetingAgenda', 'meetingDate','meetingTime' )
		labels ={
			'meetingName':('Meeting Topic'),
			'meetingAgenda':('Meeting Agenda'),
			'meetingDate':('Meeting Date'),
			'meetingTime':('Meeting Time') 
		}

# add summary when the meeting is done
#class SummaryForm(forms.ModelForm):
#
#	class Meta:
#		model = Meeting
#		fields = ('meetingSummary')