from django.http import HttpResponse, Http404
from .models import Course, Instructor, Room, MeetingTime, Department
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404
from . import scheduling
from .forms import CourseForm, InstructorForm, DepartmentForm, RoomForm, MeetingTimeForm

# Create your views here.

def index(request):  
    return render(request,'scheduling_app/index.html')

def course(request):
    courses= Course.objects.all().order_by('-id')
    instructors = Instructor.objects.all()
    departments = Department.objects.all()
    context= {
                'courses' : courses,
                'instructors' : instructors,
                'departments' : departments,
                'form':''
            }
    return render(request,'scheduling_app/courses.html',context)

def storeCourse(request):
    if request.method == 'POST':
        course=Course()
        form=CourseForm(request.POST, instance = course) 
        if form.is_valid():
            form.save()
            response = redirect('/course/')
            return response
        else:
            context= {
                'courses' : Course.objects.all().order_by('-id'),
                'instructors' : Instructor.objects.all(),
                'departments' : Department.objects.all(),
                'form':form
            }
            return render(request,'scheduling_app/courses.html',context)

def instructor(request):
    context= {
        'instructors' : Instructor.objects.all().order_by('-instructor_id')
    }   
    return render(request,'scheduling_app/instructors.html',context)

def storeInstructor(request):
    if request.method == 'POST':
        instructor=Instructor()
        form=InstructorForm(request.POST, instance = instructor) 
        if form.is_valid():
            form.save()
            return redirect('/instructor/')
        else:
            context= {
                'instructors' : Instructor.objects.all().order_by('-instructor_id'),
                'form':form
            }
            return render(request,'scheduling_app/courses.html',context)

def department(request):
    context= {
        'departments' : Department.objects.all().order_by('-id')
    }   
    return render(request,'scheduling_app/department.html',context)

def storeDepartment(request):
    if request.method == 'POST':
        department=Department()
        form=DepartmentForm(request.POST, instance = department) 
        if form.is_valid():
            form.save()
            # department.name= request.POST.get('name')
            # department= department.save()
            # print('department:', department)
            # sems=[1,2,3,4,5,6,7,8]
            # for i in range(0, len(sems)):
            #     sem=Semester()
            #     sem.department_id=department.id
            #     sem.sem=sems[i]
            #     sem.save()
            return redirect('/department/')
        else:
            context= {
                'departments' :Department.objects.all().order_by('-id'),
                'form':form
            }
            return render(request,'scheduling_app/department.html',context)

def meetingTime(request):
    context= {
        'times' : MeetingTime.objects.all().order_by('-meeting_id')
    } 
    return render(request,'scheduling_app/time.html',context)

def storeMeetingTime(request):
    if request.method == 'POST':
        time = MeetingTime()        
        time.id= request.POST.get('id')
        time.day= request.POST.get('day')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        time.time= start_time +"-"+ end_time
        time.save()
        return redirect('/meeting-time/')
    # if request.method == 'POST':
    #     print("dakandsnmmn,sad,mnmfadmma")
    #     form=MeetingTimeForm(request.POST)
    #     if form.is_valid():
    #         print("dakandsnmmn,sad,mnmfadmma")
    #         time = MeetingTime()        
    #         time.id= request.POST.get('id')
    #         time.day= request.POST.get('day')
    #         start_time = request.POST.get('start_time')
    #         end_time = request.POST.get('end_time')
    #         time.time= start_time +"-"+ end_time
    #         # print(start_time +"-"+ end_time)
    #         time.save()
    #         return redirect('/meeting-time/')
    #     else:
    #         context= {
    #             'times' : MeetingTime.objects.all().order_by('-meeting_id'),
    #             'form':form
    #         } 
    # return render(request,'scheduling_app/time.html',context)

def room(request):
    context= {
        'rooms' : Room.objects.all().order_by('-id')
    } 
    return render(request,'scheduling_app/room.html',context)

def storeRoom(request):
    if request.method == 'POST':
        room=Room()
        form=RoomForm(request.POST, instance = room) 
        if form.is_valid():
            form.save()
            return redirect('/room/')
        else:
            context= {
                'rooms' :Room.objects.all().order_by('-id'),
                'form':form
            }
            return render(request,'scheduling_app/room.html',context)

def schedule(request):
    p = ['SUN','MON','TUE','WED','THU','FRI']
    Course.objects.all().update(status=0)
    for department in request.POST.getlist('departments'):
        for sem in request.POST.getlist(department):
            Course.objects.filter(department_id=department , sem=sem).update(status=1)
    
    schedule=scheduling.generate_schedule()
    classes = schedule.get_classes()
    context={
        'classes': classes,
        'p' : p
    }
    return render(request,'scheduling_app/schedule.html',context)

def scheduleSem(request):
    depts = Department.objects.all()
    context={
        'departments': depts,
        'sems': ['1','2','3','4','5','6','7','8']
    }
    return render(request,'scheduling_app/class.html',context)