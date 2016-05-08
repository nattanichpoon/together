from django import forms

from .models import Project, Task

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('projectName','members', 'dueDate',)


class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('project','taskName','description','assignee','difficultyLevel',)

class EmailForm(forms.Form):
	email = forms.EmailField()
	message = forms.CharField()