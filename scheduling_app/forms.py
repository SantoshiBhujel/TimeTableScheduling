from django import forms
from django.forms import ModelForm

from .models import Course, Instructor, Department, Room, MeetingTime

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ('number','name','sem','instructors','department','type','maxNoOfStudents','periodPerWeek')
        

class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ('id','name')


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ('name',)
        
class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = ('number','seatingCapacity','type')

class MeetingTimeForm(forms.Form):
    id= forms.CharField()
    day= forms.CharField()
    statrt_time= forms.DateField()
    end_time= forms.DateField()
        # fields = ('number','seatingCapacity','type')