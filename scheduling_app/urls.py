from django.urls import path
from . import views

app_name = 'scheduling'

urlpatterns = [
    path('', views.index,name='index'),
    path('course/', views.course,name='course'),
    path('instructor/', views.instructor,name='instructor'),
    path('department/', views.department,name='department'),
    path('meeting-time/', views.meetingTime,name='meetingTime'),
    path('room/', views.room,name='room'),
    path('schedule/', views.schedule,name='schedule'),
]
