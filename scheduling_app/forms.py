from django import forms
from django.forms import ModelForm

from .models import Course

class CourseForm(ModelForm):
    # number = forms.CharField(max_length=200)
    # name = forms.CharField(max_length=200) 
    # sem = forms.IntegerField()# Relation ==> One interests is associated with many persons & one person have many interests.
    # instructors =forms.IntegerField()
    # department = forms.IntegerField()
    # type= forms.CharField(max_length=20)
    # max = forms.IntegerField()
    # period= forms.IntegerField()
    class Meta:
        model = Course
        fields = ('number','name','sem','instructors','department','type','maxNoOfStudents','periodPerWeek')
    
    