from django.contrib import admin
from .models import Project,Task
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('projectName', 'get_members')

class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskName', 'project', 'assignee', 'taskState')

admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
