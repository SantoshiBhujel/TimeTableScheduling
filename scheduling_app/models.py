from django.db import models

# Create your models here.
class Instructor(models.Model):
    instructor_id = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    
    def get_id(self): return self.id
    def get_name(self): return self.name
    def __str__(self): return self.name


class Room(models.Model):
    number = models.CharField(max_length=200)
    seatingCapacity = models.CharField(max_length=200)
    type= models.CharField(max_length=20,default="TH")
    
    def get_number(self): return self.number
    def get_seatingCapacity(self): return self.seatingCapacity

class MeetingTime(models.Model):
    meeting_id = models.BigAutoField(primary_key=True)
    id = models.CharField(max_length=200)
    day = models.CharField(max_length=50)
    time = models.CharField(max_length=200)
    
    def get_id(self): return self.id
    def get_time(self): return self.time 
    def __str__(self): 
        return str(self.id)
    
class Department(models.Model):
    name = models.CharField(max_length=200)
    
    def get_name(self): return self.name
    def get_courses(self): return self.courses
    def __str__(self): 
        return str(self.name)

class Course(models.Model):
    number = models.CharField(max_length=200)
    sem = models.IntegerField()
    name = models.CharField(max_length=200)                      # Relation ==> One interests is associated with many persons & one person have many interests.
    instructors = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    maxNoOfStudents = models.IntegerField(default=25)
    periodPerWeek = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    type= models.CharField(max_length=20,default="TH")
    status = models.CharField(max_length=20)
    
    def get_id(self): return self.id
    def get_name(self): return self.name
    def __str__(self): return self.name
    