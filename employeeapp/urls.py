from django.urls import path


from . import views

app_name='employeeapp'
urlpatterns=[
    path('employeehomepage',views.employeehomepagecall,name='employeehomepage'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),
    path('view_my_meetings/', views.view_my_meetings, name='view_my_meetings'),
    path('notifications/', views.notifications, name='notifications'),
    path('view_reports/', views.view_reports, name='view_reports'),
    path('sessions/', views.employee_sessions, name='employee_sessions'),
    path('my-programs/', views.employee_programs, name='employee_programs'),
    path('create-profile/', views.create_or_update_profile, name='create_profile'),
    path('view-profile/', views.view_profile, name='view_profile'),
    path('certificates/', views.view_certificates, name='view_certificates'),
    path('courses/', views.employee_courses, name='employee_courses'),

]
