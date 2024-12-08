from django import forms
from .models import Trainer

class TrainerProfileForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['specialization', 'experience_years', 'contact_number', 'profile_picture']
from django import forms
from .models import Meeting
from employeeapp.models import Course
class ScheduleMeetingForm(forms.ModelForm):
    class Meta:
        model = Meeting
        fields = ['title', 'description', 'date', 'time', 'meeting_link', 'email']


class AssignCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'duration']  # Ensure that these fields exist in your model
from django import forms
from .models import Certificate

class CertificateForm(forms.ModelForm):
    class Meta:
        model = Certificate
        fields = ['employee', 'title', 'certificate_file']
from django import forms
from employeeapp.models import Course

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'start_date', 'end_date', 'duration']
