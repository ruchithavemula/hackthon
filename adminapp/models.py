from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username


class Meeting(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='meetings')

    def __str__(self):
        return self.title
class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

    def __str__(self):
        return self.title


class Report(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reports')

    def __str__(self):
        return self.title

class Session(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    duration = models.DurationField()  # Time duration of the session
    assigned_employees = models.ManyToManyField(Employee, related_name='assigned_sessions')

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

class TrainingProgram(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    trainer = models.CharField(max_length=255)
    time = models.DateTimeField()
    employees = models.ManyToManyField(User, related_name='training_programs')

    def __str__(self):
        return self.name
