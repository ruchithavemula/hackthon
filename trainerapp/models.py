
from django.db import models
from django.contrib.auth.models import User
from employeeapp.models import Course

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=255)
    experience_years = models.IntegerField()
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='trainer_profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.username

class CourseAssignment(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trainer.user.username} assigned {self.course.title} to {self.employee.username}"

from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    meeting_link = models.URLField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

class Certificate(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    title = models.CharField(max_length=255)
    issue_date = models.DateField(auto_now_add=True)
    certificate_file = models.FileField(upload_to='certificates/')
