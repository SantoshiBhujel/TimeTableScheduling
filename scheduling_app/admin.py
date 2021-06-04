from django.contrib import admin
from .models import Course, Instructor, Room, MeetingTime, Department
# Register your models here.

admin.site.register(Course)
admin.site.register(Instructor)
admin.site.register(Room)
admin.site.register(MeetingTime)
admin.site.register(Department)