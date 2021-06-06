from django.http import HttpResponse, Http404
from .models import Course, Instructor, Room, MeetingTime, Department
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from . import scheduling

# Create your views here.

def index(request):  
    return render(request,'scheduling_app/index.html')

def course(request):
    if request.method == 'POST':
        print("inside post")
        course=Course()
        course.number= request.POST.get('number')
        course.sem= request.POST.get('sem')
        course.name= request.POST.get('name')
        course.maxNoOfStudents= request.POST.get('max')
        course.periodPerWeek= request.POST.get('period')
        course.department_id= request.POST.get('department')
        course.instructors_id = request.POST.get('instructors')
        course.type = request.POST.get('type')
        course.save()
        
    courses= Course.objects.all().order_by('-id')
    instructors = Instructor.objects.all()
    departments = Department.objects.all()
    context= {
        'courses' : courses,
        'instructors' : instructors,
        'departments' : departments
    }  
    return render(request,'scheduling_app/courses.html',context)

def instructor(request):
    if request.method == 'POST':
        instructor=Instructor()
        instructor.id= request.POST.get('id')
        instructor.name= request.POST.get('name')
        instructor.save()
    instructors = Instructor.objects.all().order_by('-instructor_id')
    context= {
        'instructors' : instructors
    }   
    return render(request,'scheduling_app/instructors.html',context)

def department(request):
    if request.method == 'POST':
        department = Department()        
        department.name= request.POST.get('name')
        department.save()
        
    departments = Department.objects.all().order_by('-id')
    context= {
        'departments' : departments
    }   
    return render(request,'scheduling_app/department.html',context)

def meetingTime(request):
    if request.method == 'POST':
        time = MeetingTime()        
        time.id= request.POST.get('id')
        time.day= request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        time.time= start_time +"-"+ end_time
        # print(start_time +"-"+ end_time)
        time.save()
    times = MeetingTime.objects.all().order_by('-meeting_id')
    context= {
        'times' : times
    } 
    return render(request,'scheduling_app/time.html',context)

def room(request):
    if request.method == 'POST':
        room = Room()        
        room.number= request.POST.get('number')
        room.seatingCapacity= request.POST.get('capacity')
        room.type = request.POST.get('type')
        room.save()
        
    rooms = Room.objects.all().order_by('-id')
    context= {
        'rooms' : rooms
    } 
    return render(request,'scheduling_app/room.html',context)

def schedule(request):
    p = ['SUN','MON','TUE','WED','THU','FRI']
    schedule=scheduling.generate_schedule()
    classes = schedule.get_classes()
    context={
        'classes': classes,
        'p' : p
    }
    return render(request,'scheduling_app/schedule.html',context)