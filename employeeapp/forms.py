from django import forms
from .models import Enrollment, Course


class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['course']

    course = forms.ModelChoiceField(queryset=Course.objects.all(), empty_label="Select a Course")

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CourseEnrollmentForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        enrollment = super(CourseEnrollmentForm, self).save(commit=False)
        enrollment.user = self.user
        if commit:
            enrollment.save()
        return enrollment
from django import forms
from .models import EmployeeProfile

class EmployeeProfileForm(forms.ModelForm):
    class Meta:
        model = EmployeeProfile
        fields = ['job_title', 'department', 'contact_number', 'address', 'profile_picture']
