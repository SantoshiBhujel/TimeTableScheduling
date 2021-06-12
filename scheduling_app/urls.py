from django.urls import path
from . import views

app_name = 'scheduling'

urlpatterns = [
    path('', views.index,name='index'),
    path('course/', views.course,name='course'),
    path('course/store', views.storeCourse,name='storeCourse'),
    path('instructor/', views.instructor,name='instructor'),
    path('instructor/store', views.storeInstructor,name='storeInstructor'),
    path('department/', views.department,name='department'),
    path('department/store', views.storeDepartment,name='storeDepartment'),
    path('meeting-time/', views.meetingTime,name='meetingTime'),
    path('meeting-time/store', views.storeMeetingTime,name='storeMeetingTime'),
    path('room/', views.room,name='room'),
    path('room/store', views.storeRoom,name='storeRoom'),
    path('schedule/classes', views.scheduleSem,name='scheduleSem'),
    path('schedule/', views.schedule,name='schedule'),
]
