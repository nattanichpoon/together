from django import forms

from .models import Project, Task

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('projectName','members', 'dueDate', 'grabBy')


class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
<<<<<<< HEAD
		fields = ('taskName','assignee','description','difficultyLevel','project', 'taskState')
=======
		fields = ('project','taskName','description','assignee','difficultyLevel',)

class EmailForm(forms.Form):
	email = forms.EmailField()
	message = forms.CharField()
>>>>>>> poon-new-p
