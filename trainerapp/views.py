from django.contrib.auth.models import User


def trainerhomepagecall(request):
    return render(request,'trainerapp/trainerhomepage.html')

def trainer_dashboard(request):
    return render(request, 'trainerapp/trainer_dashboard.html')

from django.shortcuts import get_object_or_404
from .models import Trainer
from .forms import TrainerProfileForm
from django.contrib.auth.decorators import login_required


@login_required
def create_trainer_profile(request):
    if request.method == "POST":
        form = TrainerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            trainer = form.save(commit=False)
            trainer.user = request.user
            trainer.save()
            messages.success(request, "Trainer profile created successfully!")
            return redirect('trainerapp:view_trainer_profile')
    else:
        form = TrainerProfileForm()
    return render(request, 'trainerapp/create_trainer_profile.html', {'form': form})

@login_required
def view_trainer_profile(request):
    trainer = get_object_or_404(Trainer, user=request.user)
    return render(request, 'trainerapp/view_trainer_profile.html', {'trainer': trainer})

@login_required
def update_trainer_profile(request):
    trainer = get_object_or_404(Trainer, user=request.user)
    if request.method == "POST":
        form = TrainerProfileForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            messages.success(request, "Trainer profile updated successfully!")
            return redirect('trainerapp:view_trainer_profile')
    else:
        form = TrainerProfileForm(instance=trainer)
    return render(request, 'trainerapp/update_trainer_profile.html', {'form': form})

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import ScheduleMeetingForm
from .models import Meeting

@login_required
def schedule_meeting(request):
    if request.method == "POST":
        form = ScheduleMeetingForm(request.POST)
        if form.is_valid():
            meeting = form.save()
            recipient_email = form.cleaned_data.get('email')

            send_mail(
                subject=f"Meeting Scheduled: {meeting.title}",
                message=f"You are invited to the meeting.\n\n"
                        f"Title: {meeting.title}\n"
                        f"Description: {meeting.description}\n"
                        f"Date: {meeting.date}\n"
                        f"Time: {meeting.time}\n"
                        f"Meeting Link: {meeting.meeting_link}",
                from_email='your-email@example.com',
                recipient_list=[recipient_email],
            )
            return redirect('trainerapp:meeting_list')
    else:
        form = ScheduleMeetingForm()

    return render(request, 'trainerapp/schedule_meeting.html', {'form': form})


def send_meeting_email(meeting):
    subject = f"Meeting Scheduled: {meeting.title}"
    message = f"""
    Hello {meeting.employee.get_full_name()},

    A new meeting has been scheduled for you:

    Title: {meeting.title}
    Description: {meeting.description}
    Date: {meeting.date}
    Time: {meeting.time}
    Meeting Link: {meeting.meeting_link}

    Please join the meeting on time.

    Best regards,
    Trainer Team
    """
    recipient_email = meeting.employee.email
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [recipient_email])

@login_required
def meeting_list(request):
    meetings = Meeting.objects.all()
    return render(request, 'trainerapp/meeting_list.html', {'meetings': meetings})

@login_required
def employee_meetings(request, employee_id):
    meetings = Meeting.objects.filter(employee_id=employee_id)
    return render(request, 'trainerapp/employee_meetings.html', {'meetings': meetings})

from django.contrib.auth.decorators import login_required

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from .models import CourseAssignment
from django.contrib.auth.models import User

@login_required
def assigned_course_list(request):
    # Retrieve the courses assigned by the logged-in trainer
    if request.user.groups.filter(name='trainer').exists():
        assigned_courses = CourseAssignment.objects.filter(trainer__user=request.user)
    # Retrieve the courses assigned to the logged-in employee
    elif request.user.groups.filter(name='employee').exists():
        assigned_courses = CourseAssignment.objects.filter(employee=request.user)
    else:
        assigned_courses = CourseAssignment.objects.none()

    return render(request, 'trainerapp/assigned_course_list.html', {'assigned_courses': assigned_courses})


from django.shortcuts import render

# Define the correct answers to the assignment questions
CORRECT_ANSWERS = {
    'q1': 'a',
    'q2': 'b',
    'q3': 'b',
    'q4': 'c',
    'q5': 'a',
    'q6': 'd',
    'q7': 'b',
    'q8': 'b',
    'q9': 'a',
    'q10': 'b',
}


# Function to evaluate the answers and calculate progress
def evaluate_answers(user_answers):
    correct_count = 0
    for key, correct_answer in CORRECT_ANSWERS.items():
        if user_answers.get(key) == correct_answer:
            correct_count += 1

    wrong_count = len(CORRECT_ANSWERS) - correct_count
    return correct_count, wrong_count


# View to render the assignment form and calculate progress
def assignment_view(request):
    if request.method == "POST":
        # Get user-submitted answers
        user_answers = {
            'q1': request.POST.get('q1'),
            'q2': request.POST.get('q2'),
            'q3': request.POST.get('q3'),
            'q4': request.POST.get('q4'),
            'q5': request.POST.get('q5'),
            'q6': request.POST.get('q6'),
            'q7': request.POST.get('q7'),
            'q8': request.POST.get('q8'),
            'q9': request.POST.get('q9'),
            'q10': request.POST.get('q10'),
        }

        # Evaluate the answers
        correct_count, wrong_count = evaluate_answers(user_answers)
        total_questions = len(CORRECT_ANSWERS)

        # Calculate percentages
        correct_percentage = (correct_count / total_questions) * 100
        wrong_percentage = (wrong_count / total_questions) * 100

        # Send the percentages to the template
        context = {
            'correct_percentage': correct_percentage,
            'wrong_percentage': wrong_percentage,
            'correct_count': correct_count,
            'wrong_count': wrong_count,
        }
        return render(request, 'trainerapp/progress.html', context)

    # If GET request, show the assignment form
    return render(request, 'trainerapp/assignment.html')

from django.shortcuts import render, redirect
from .forms import CertificateForm

def upload_certificate(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('trainerapp:certificate_success')
    else:
        form = CertificateForm()
    return render(request, 'trainerapp/upload_certificate.html', {'form': form})

def certificate_success(request):
    return render(request, 'trainerapp/certificate_success.html')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employeeapp.models import Course
from .forms import AddCourseForm

@login_required
def add_course(request):
    if request.method == 'POST':
        form = AddCourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.user = request.user
            course.save()
            return redirect('trainerapp:added_courses')
    else:
        form = AddCourseForm()
    return render(request, 'trainerapp/add_course.html', {'form': form})

@login_required
def added_courses(request):
    courses = Course.objects.filter(user=request.user)
    return render(request, 'trainerapp/added_courses.html', {'courses': courses})
