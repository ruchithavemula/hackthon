from django import forms

from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'phone_number', 'role']

from django import forms
from .models import Meeting

class ScheduleMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'description', 'date', 'time', 'employee']
from django import forms
from .models import Notification

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ['employee', 'title', 'message']

from django import forms
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['employee', 'title', 'content']

from django import forms
from .models import Session, Employee

class AssignSessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['title', 'description', 'duration', 'assigned_employees']

    assigned_employees = forms.ModelMultipleChoiceField(
        queryset=Employee.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
from django import forms
from .models import TrainingProgram

class TrainingProgramForm(forms.ModelForm):
    class Meta:
        model = TrainingProgram
        fields = ['name', 'title', 'trainer', 'time', 'employees']
        widgets = {
            'time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'employees': forms.CheckboxSelectMultiple(),
        }
