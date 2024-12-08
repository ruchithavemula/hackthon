def homepagecall(request):
    return render(request,'adminapp/projecthomepage.html')



def loginpagecall(request):
    return render(request,'adminapp/LoginPage.html')

def registerpagecall(request):
    return render(request, 'adminapp/Register.html')


import re
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User


def UserRegisterLogic(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        pass1 = request.POST['password']
        pass2 = request.POST['password1']

        # Validate first name and last name (only letters allowed)
        if not re.match("^[A-Za-z]+$", first_name):
            messages.info(request, 'First name can only contain letters.')
            return render(request, 'adminapp/Register.html')

        if not re.match("^[A-Za-z]+$", last_name):
            messages.info(request, 'Last name can only contain letters.')
            return render(request, 'adminapp/Register.html')

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'OOPS! Username already taken.')
                return render(request, 'adminapp/Register.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'OOPS! Email already registered.')
                return render(request, 'adminapp/Register.html')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=pass1,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.info(request, 'Account created Successfully!')
                return render(request, 'adminapp/projectHomePage.html')
        else:
            messages.info(request, 'Passwords do not match.')
            return render(request, 'adminapp/Register.html')
    else:
        return render(request, 'adminapp/Register.html')


def UserLoginLogic(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)


            if len(username) == 10:
                messages.success(request, 'Login successful as student!')
                return redirect('trainerapp:trainerhomepage')
            elif len(username) == 4:
                messages.success(request, 'Login successful as faculty!')
                return redirect('employeeapp:employeehomepage')
            elif len(username) == 5:
                messages.success(request, 'Login successful as admin!')
                return redirect('adminapp:admin_dashboard')
            else:
                messages.error(request, 'Username length does not match student, faculty, or admin criteria.')
                return render(request, 'adminapp/LoginPage.html')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'adminapp/LoginPage.html')
    else:
        return render(request, 'adminapp/LoginPage.html')

def user_logout(request):
    auth.logout(request)
    return redirect('adminapp:projecthomepage')

from django.contrib.auth.decorators import login_required

@login_required
def admin_dashboard(request):
    return render(request, 'adminapp/admin_dashboard.html')

@login_required
def adminhomepage(request):
    return render(request, 'adminapp/adminhomepage.html')
def trainer_dashboard(request):
    return render(request, 'adminapp/trainer_dashboard.html')

def employee_dashboard(request):
    return render(request, 'adminapp/employee_dashboard.html')

from django.contrib.auth.models import  auth
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def trainer_dashboard(request):
    return render(request, 'adminapp/trainer_dashboard.html')

from django.contrib import messages
from django.contrib.auth.models import User


def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            messages.success(request, f"Employee {employee.user.username} added successfully!")
            return redirect('adminapp:view_employee')  # Redirect to the view employee page after adding
        else:
            messages.error(request, "Error adding employee.")
    else:
        form = EmployeeForm()

    return render(request, 'adminapp/add_employee.html', {'form': form})

def view_employee(request):
    employees = Employee.objects.all()
    return render(request, 'adminapp/view_employee.html', {'employees': employees})

from .models import Employee

def delete_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        employee.delete()
        return redirect('employee_list')  # Redirect to the employee list page
    return render(request, 'adminapp/delete_employee.html', {'employee': employee})
from .forms import EmployeeForm

def update_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('adminapp/employee_list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'adminapp/update_employee.html', {'form': form, 'employee': employee})
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'adminapp/employee_list.html', {'employees': employees})

from .models import Meeting
from .forms import ScheduleMeetingForm

def schedule_meeting(request):
    if request.method == 'POST':
        form = ScheduleMeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp:view_meetings')
    else:
        form = ScheduleMeetingForm()
    return render(request, 'adminapp/schedule_meeting.html', {'form': form})

def view_meetings(request):
    meetings = Meeting.objects.all()
    return render(request, 'adminapp/view_meetings.html', {'meetings': meetings})

from .forms import NotificationForm
from .models import Notification
from .forms import NotificationForm
from .models import Notification
from django.shortcuts import render, redirect
from django.contrib import messages


def send_notifications(request):
    try:
        if request.method == 'POST':
            form = NotificationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Notification sent successfully.")
                return redirect('adminapp:view_notifications')
            else:
                messages.error(request, "Error sending notification. Please check the form.")
        else:
            form = NotificationForm()
    except Exception as e:
        messages.error(request, f"An error occurred: {e}")
        return render(request, 'adminapp/send_notifications.html', {'form': form})

    return render(request, 'adminapp/send_notifications.html', {'form': form})


def view_notifications(request):
    try:
        notifications = Notification.objects.all()
    except Exception as e:
        messages.error(request, f"An error occurred while fetching notifications: {e}")
        notifications = []

    return render(request, 'adminapp/view_notifications.html', {'notifications': notifications})


def create_report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp:report_list')
    else:
        form = ReportForm()
    return render(request, 'adminapp/create_report.html', {'form': form})

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'adminapp/report_list.html', {'reports': reports})

from .forms import ReportForm

def update_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        form = ReportForm(request.POST, instance=report)
        if form.is_valid():
            form.save()
            return redirect('adminapp:report_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'adminapp/update_report.html', {'form': form, 'report': report})

def delete_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    if request.method == "POST":
        report.delete()
        return redirect('adminapp:report_list')
    return render(request, 'adminapp/delete_report.html', {'report': report})

from django.shortcuts import render, get_object_or_404
from .models import Report

def view_report(request, pk):
    report = get_object_or_404(Report, pk=pk)
    return render(request, 'adminapp/view_report.html', {'report': report})


from .forms import AssignSessionForm
from .models import Session
from django.contrib.auth.decorators import login_required

@login_required
def assign_session(request):
    if request.method == "POST":
        form = AssignSessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp:session_list')
    else:
        form = AssignSessionForm()
    return render(request, 'adminapp/assign_session.html', {'form': form})

@login_required
def session_list(request):
    sessions = Session.objects.all()
    return render(request, 'adminapp/session_list.html', {'sessions': sessions})
from django.shortcuts import render, redirect
from .models import TrainingProgram
from .forms import TrainingProgramForm

def program_list(request):
    programs = TrainingProgram.objects.all()
    return render(request, 'adminapp/program_list.html', {'programs': programs})

def add_program(request):
    if request.method == 'POST':
        form = TrainingProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('adminapp:program_list')
    else:
        form = TrainingProgramForm()
    return render(request, 'adminapp/add_program.html', {'form': form})
