from django.urls import path
from . import views
from.views import assignment_view
app_name='trainerapp'
urlpatterns=[
    path('trainerhomepage',views.trainerhomepagecall,name='trainerhomepage'),
    path('trainer_dashboard/', views.trainer_dashboard, name='trainer_dashboard'),
    path('create/', views.create_trainer_profile, name='create_trainer_profile'),
    path('view/', views.view_trainer_profile, name='view_trainer_profile'),
    path('update/', views.update_trainer_profile, name='update_trainer_profile'),
    path('schedule-meeting/', views.schedule_meeting, name='schedule_meeting'),
    path('meetings/', views.meeting_list, name='meeting_list'),
    path('employee-meetings/<int:employee_id>/', views.employee_meetings, name='employee_meetings'),

    path('assigned-courses/', views.assigned_course_list, name='assigned_courses'),
    path('assignment/', views.assignment_view, name='assignment'),
    path('upload-certificate/', views.upload_certificate, name='upload_certificate'),
    path('certificate-success/', views.certificate_success, name='certificate_success'),
    path('add_course/', views.add_course, name='add_course'),
    path('added_courses/', views.added_courses, name='added_courses'),
]