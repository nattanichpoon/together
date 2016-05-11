from django import forms

from .models import Project, Task

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('projectName','members', 'dueDate', 'grabBy')


class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('project','taskName','description','assignee','difficultyLevel', 'expectedDate','taskState', 'taskProgress')

class EmailForm(forms.Form):
	email = forms.EmailField()
	message = forms.CharField()

class TaskFormNew(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('taskName','description','assignee','difficultyLevel', 'expectedDate','taskState')