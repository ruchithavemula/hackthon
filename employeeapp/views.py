from django.contrib import messages

from .models import Course, Enrollment
from trainerapp.models import Certificate

def employeehomepagecall(request):
    return render(request, 'employeeapp/employeehomepage.html')



def employee_dashboard(request):
    courses = Enrollment.objects.filter(user=request.user, completed=False)
    context = {
        'courses': courses
    }
    return render(request, 'employeeapp/employee_dashboard.html', context)

from adminapp.models import Meeting
from django.contrib.auth.decorators import login_required

@login_required
def view_my_meetings(request):
    meetings = Meeting.objects.filter(employee=request.user)
    return render(request, 'employeeapp/view_my_meetings.html', {'meetings': meetings})

from adminapp.models import Notification
from django.contrib.auth.decorators import login_required

@login_required
def notifications(request):

    notifications = Notification.objects.filter(employee=request.user)
    return render(request, 'employeeapp/notifications.html', {'notifications': notifications})
from adminapp.models import Report
from django.contrib.auth.decorators import login_required
@login_required
def view_reports(request):
    employee = request.user.employee
    reports = Report.objects.filter(employee=employee)
    return render(request, 'employeeapp/view_reports.html', {'reports': reports})

from adminapp.models import Employee
from django.contrib.auth.decorators import login_required
@login_required
def employee_sessions(request):
    employee = Employee.objects.get(user=request.user)
    assigned_sessions = employee.assigned_sessions.all()
    return render(request, 'employeeapp/employee_sessions.html', {'assigned_sessions': assigned_sessions})

from adminapp.models import TrainingProgram
from django.contrib.auth.decorators import login_required
@login_required
def employee_programs(request):
    programs = TrainingProgram.objects.filter(employees=request.user)
    return render(request, 'employeeapp/employee_programs.html', {'programs': programs})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import EmployeeProfile
from .forms import EmployeeProfileForm
@login_required
def create_or_update_profile(request):
    profile, created = EmployeeProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = EmployeeProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('employeeapp:view_profile')
    else:
        form = EmployeeProfileForm(instance=profile)
    return render(request, 'employeeapp/create_profile.html', {'form': form})

@login_required
def view_profile(request):
    profile = get_object_or_404(EmployeeProfile, user=request.user)
    return render(request, 'employeeapp/view_profile.html', {'profile': profile})


@login_required
def view_course_content(request, course_id):
    course = Course.objects.get(id=course_id)
    return render(request, 'employeeapp/view_course_content.html', {'course': course})


@login_required
def complete_course(request, course_id):
    enrollment = Enrollment.objects.get(user=request.user, course_id=course_id)
    enrollment.completed = True
    enrollment.save()

    # Check if the employee has completed all courses
    if not Enrollment.objects.filter(user=request.user, completed=False).exists():
        Certificate.objects.create(user=request.user, course=enrollment.course, issued_date=timezone.now())
        messages.success(request, "You have completed all courses and received your certificate!")

    return redirect('employeeapp:employee_dashboard')
from django.shortcuts import render
from trainerapp.models import Certificate

def view_certificates(request):
    certificates = Certificate.objects.filter(employee=request.user)
    return render(request, 'employeeapp/view_certificates.html', {'certificates': certificates})
from django.shortcuts import render
from employeeapp.models import Course

def employee_courses(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'employeeapp/employee_courses.html', {'courses': courses})
