from django.contrib import admin
from schedule1.models import Date, Album, Song, Meeting
# Register your models here.
admin.site.register(Date)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Meeting)

class MeetingAdmin(admin.ModelAdmin):
	list_display = ('meetingName','project','meetingDate','meetingStatus','confirmedCount')