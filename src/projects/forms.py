from django import forms

from .models import Project, Task

class ProjectForm(forms.ModelForm):
	# members = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)

    class Meta:
        model = Project
        dueDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
        fields = ('projectName','members', 'dueDate', 'grabBy')
        # widgets = {
        # 'dueDate': forms.DateInput(attrs = {'class':'datepicker'})
        # }


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