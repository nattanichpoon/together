from django.contrib import admin
from schedule1.models import Meeting
# Register your models here.

admin.site.register(Meeting)

class MeetingAdmin(admin.ModelAdmin):
	list_display = ('meetingName','project','meetingDate','meetingStatus','confirmedCount')