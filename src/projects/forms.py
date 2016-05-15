from django import forms

from .models import Project, Task
from django.forms.widgets import CheckboxInput

def make_custom_datefield(f):
    # f is a model field
    # if f is a date field, add the datepicker class to it
    # return a form field
    formfield = f.formfield()
    if isinstance(f, models.DateField):
        formfield.widget.attrs.update({'class':'datePicker'})
    return formfield

class ProjectForm(forms.ModelForm):
	# members = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
	# dueDate_callback = make_custom_datefield(self)

	class Meta:
		model = Project
		dueDate = forms.DateField(widget=forms.DateInput(attrs={'class': 'datepicker'}))
		fields = ('projectName','members', 'dueDate', 'grabBy')
		widgets = {
        	# 'members' : forms.CheckboxSelectMultiple(),
        	'dueDate': forms.DateInput(attrs = {'class':'datepicker'})
        }


class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = ('project','taskName','description','assignee','difficultyLevel', 'expectedDate','taskState', 'taskProgress')
	

class EmailForm(forms.Form):
	email = forms.EmailField()
	message = forms.CharField()

class TaskFormNew(forms.ModelForm):
	# assignee = MyFormField()
	# assignee = ModelMultipleChoiceField(queryset = Projects.objects.all())
	class Meta:
		model = Task
		fields = ('taskName','description','assignee','difficultyLevel', 'expectedDate','taskState')

		labels = {
			'taskName' : ('Task Name'),
			# 'description' : ('What to do for this task?'),
			'assignee' : ('Who\'s working on it?'),
			'difficultyLevel' : ('Difficulty Level'),
			'expectedDate' : ('Should be done by'),
			'taskState' : ('Task Status')
		}

		# widgets = {
		# 	'assignee' : forms.CheckboxInput(),
		# 	'expectedDate' : forms.DateInput(attrs={'class':'datepicker'})
		# 		# forms.DateInput(attrs={'type':'date'})
		# }

	# def __init__(self, *args, **kwargs):
	# 	self.project = kwargs.pop('project')
	# 	super(TaskFormNew, self).__init__(*args, **kwargs)
	#     # self.fields["assignee"].widget = CheckboxInput()
	# 	self.fields["assignee"].queryset = Project.objects.filter(pk=pk)
	# 	