# from scheduling.scheduling_app.views import course
import prettytable as prettytable
import random as rnd
from scheduling_app.models import Course as C, Instructor as I, Room as R, MeetingTime as MT, Department as D

POPULATION_SIZE = 15
NUMB_OF_ELITE_SCHEDULES = 1
TOURNAMENT_SELECTION_SIZE = 3
MUTATION_RATE = 0.01
class Data:
    def __init__(self):
        self._rooms = []; self._meetingTimes=[]; self._instructors= []; self._courses=[];
        self._depts= [];
        rooms = R.objects.all()
        instructors = I.objects.all()
        # courses = C.objects.filter(status=1)
        departments = D.objects.all()
        times = MT.objects.all()

        for room in rooms:
            self._rooms.append(Room(room.number, room.seatingCapacity, room.type)) #print(self.ROOMS[0][0], self.ROOMS[0][1]) print(self._rooms)
        
        for time in times:
            self._meetingTimes.append(MeetingTime(time.id, time.day, time.time))

        for instructor in instructors:
            self._instructors.append(Instructor(instructor.id, instructor.name))  

        # for i in range(len(courses)):
        #     self._courses.append(Course(courses[i].number, courses[i].name, courses[i].sem,[Instructor(courses[i].instructors.id,courses[i].instructors.name)],courses[i].maxNoOfStudents, courses[i].periodPerWeek, courses[i].type)) #[] removed from instructor     
        
        self._dept_course=[]
        for i in range(len(departments)):
            for courses in departments[i].course_set.all():
                if courses.status==str(1):
                    self._dept_course.append(Course(courses.number, courses.name, courses.sem,[Instructor(courses.instructors.id,courses.instructors.name)],courses.maxNoOfStudents, courses.periodPerWeek, courses.type))
            self._depts.append(Department(departments[i].name,self._dept_course))
            self._dept_course=[]
        
        self._numberOfClasses=0
        for i in range(0,len(self._depts)):
            self._numberOfClasses +=len(self._depts[i].get_courses())
            
    def get_rooms(self): return self._rooms
    def get_instructors(self): return self._instructors
    # def get_courses(self): return self._courses
    def get_depts(self): return self._depts
    def get_meetingTimes(self): return self._meetingTimes
    def get_numberOfClasses(self): return self._numberOfClasses
class Schedule:
    def __init__(self):
        self._data = main_Data() #data= Data() initialized below classes
        self._classes=[]
        self._numbOfConflicts= 0
        self._fitness = -1
        self._classNumb = 0
        self._isFitnessChanged = True
        self._rooms= main_Data().get_rooms()
        self._meetingTimes = main_Data().get_meetingTimes()
        self._room_time = []
        self._lab_time =[]
        for i in range(0, len(self._rooms)):
            if self._rooms[i].get_type()=="TH":
                for j in range(0, len(self._meetingTimes)):
                    self._room_time.append([self._rooms[i], self._meetingTimes[j]])
            if self._rooms[i].get_type()=="LAB":
                for j in range(0, len(self._meetingTimes)):
                    self._lab_time.append([self._rooms[i], self._meetingTimes[j]])
    
        # print(self._room_time)
    def get_classes(self):
        self._isFitnessChanged = True
        return self._classes
    def get_numbOfConflicts(self): return self._numbOfConflicts
    def get_fitness(self): 
        if(self._isFitnessChanged == True):
            self._fitness = self.calculate_fitness()
            self._isFitnessChanged = False
        return self._fitness
    def get_roomTime(self): return self._room_time
    def get_labTime(self): return self._lab_time
    def initialize(self):
        depts = self._data.get_depts()
        room_time = self.get_roomTime()
        lab_time = self.get_labTime()
        for i in range(0, len(depts)):
            courses = depts[i].get_courses() #courses of each department
            for j in range(0, len(courses)): #for each courses (of a department retrieved from data)
                for k in range(0,courses[j].get_periodPerWeek()):
                    newClass = Class(self._classNumb, depts[i], courses[j]) # initialize new Class(with dept[i] and courses[j] i.e. every department ko every course)
                    self._classNumb += 1
                    if courses[j].get_type()=="TH":
                        randomIndex=rnd.randrange(0,len(room_time))
                        newClass.set_meetingTime(room_time[randomIndex][1])
                        newClass.set_room(room_time[randomIndex][0])
                        newClass.set_instructor(courses[j].get_instructors()[rnd.randrange(0,len(courses[j].get_instructors()))])
                        room_time.pop(randomIndex)
                        # self._classes.append(newClass)
                    if courses[j].get_type()=="LAB":
                        randomIndex=rnd.randrange(0,len(lab_time))
                        newClass.set_meetingTime(lab_time[randomIndex][1])
                        newClass.set_room(lab_time[randomIndex][0])
                        newClass.set_instructor(courses[j].get_instructors()[rnd.randrange(0,len(courses[j].get_instructors()))])
                        lab_time.pop(randomIndex)
                        
                    # for i in range(0,len(self._classes)):
                    #     if self._classes[i].get_course().get_sem()==newClass.get_course().get_sem() and self._classes[i].get_meetingTime()== newClass.get_MeetingTime():
                    #         self.set_Class()
                    self._classes.append(newClass)          
        return self
    def calculate_fitness(self):
        self._numbOfConflicts= 0
        classes=  self.get_classes()
        for i in range(0,len(classes)):
            if (int(classes[i].get_room().get_seatingCapacity()) < int(classes[i].get_course().get_maxNumbOfStudents())):
                self._numbOfConflicts += 1
            for j in range(0, len(classes)):
                if(j>=i):
                    if(classes[i].get_meetingTime() == classes[j].get_meetingTime() and classes[i].get_id() != classes[j].get_id()):
                        # if(classes[i].get_room()== classes[j].get_room() or classes[i].get_instructor()== classes[j].get_instructor()) : 
                        #     self._numbOfConflicts +=1
                        # if(classes[i].get_instructor()== classes[j].get_instructor()) : 
                        #     self._numbOfConflicts += 1
                        if(classes[i].get_dept()== classes[j].get_dept() and classes[i].get_course().get_sem()== classes[j].get_course().get_sem()) : 
                            self._numbOfConflicts += 1
                            # print(classes[i],"sem:",classes[i].get_course().get_sem(),"\n")
                            # print(classes[j],"sem:",classes[j].get_course().get_sem(),"\n")
                            # print("sem error")
        return 1/(self._numbOfConflicts+1)
    def __str__(self):
        returnvalue=""
        for i in range(0, len(self._classes)-1):
            returnvalue += str(self._classes[i]) + ","
        returnvalue += str(self._classes[len(self._classes)-1])
        return returnvalue
class Population:
    def __init__(self,size): 
        self._size = size
        self._data = main_Data()
        self._schedules= []
        for i in range(0, size):
            self._schedules.append(Schedule().initialize())
    def get_schedules(self): return self._schedules
class GeneticAlgorithm:
    def evolve(self, population):
        return self._mutate_population(self._crossover_population(population))
    def _crossover_population(self,pop):
	    crossover_pop = Population(0)
	    for i in range(NUMB_OF_ELITE_SCHEDULES):
		    crossover_pop.get_schedules().append(pop.get_schedules()[i])
	    i = NUMB_OF_ELITE_SCHEDULES
	    while i < POPULATION_SIZE:
		    schedule1 = self._select_tournament_population(pop).get_schedules()[0] 
		    schedule2 = self._select_tournament_population(pop).get_schedules()[0]
		    crossover_pop.get_schedules().append(self._crossover_schedule(schedule1, schedule2))
		    i += 1
	    return crossover_pop
    def _mutate_population(self,population):
        for i in range(NUMB_OF_ELITE_SCHEDULES, POPULATION_SIZE):
            self._mutate_schedule(population.get_schedules()[i])
            return population
    def _crossover_schedule(self,schedule1,schedule2):
        crossoverSchedule = Schedule().initialize()
        for i in range(0, len(crossoverSchedule.get_classes())):
            if (rnd.random() > 0.5): crossoverSchedule.get_classes()[i] = schedule1.get_classes()[i]
            else: crossoverSchedule.get_classes()[i] = schedule2.get_classes()[i]
            return crossoverSchedule
    def _mutate_schedule(self, mutateSchedule):
        schedule = Schedule().initialize()
        for i in range(0, len(mutateSchedule.get_classes())):
            if(MUTATION_RATE > rnd.random()): mutateSchedule.get_classes()[i] = schedule.get_classes()[i]
            return mutateSchedule
    def _select_tournament_population(self, pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_schedules().append(pop.get_schedules()[rnd.randrange(0, POPULATION_SIZE)])
            i += 1
            tournament_pop.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
            return tournament_pop
class Course:
    def __init__(self, number, name, sem, instructors, maxNumbOfStudents,periodPerWeek, type):
        self._number = number
        self._name = name
        self._sem = sem
        self._instructors= instructors
        self._maxNumbOfStudents = maxNumbOfStudents
        self._periodPerWeek = periodPerWeek
        self._type = type
    def get_number(self): return self._number
    def get_name(self): return self._name
    def get_sem(self): return self._sem
    def get_instructors(self): return self._instructors
    def get_maxNumbOfStudents(self): return self._maxNumbOfStudents
    def get_periodPerWeek(self): return self._periodPerWeek
    def get_type(self): return self._type
    def __str__(self): return self._name
class Instructor:
    def __init__(self, id, name):
        self._id = id
        self._name = name
    def get_id(self): return self._id
    def get_name(self): return self._name
    def __str__(self): return self._name
class Room:
    def __init__(self, number, seatingCapacity, type):
        self._number = number
        self._seatingCapacity = seatingCapacity
        self._type = type
    def get_number(self): return self._number
    def get_seatingCapacity(self): return self._seatingCapacity
    def get_type(self): return self._type
class MeetingTime:
    def __init__(self, id, day, time):
        self._id = id
        self._day = day
        self._time = time
    def get_id(self): return self._id
    def get_day(self): return self._day
    def get_time(self): return self._time  
class Department:
    def __init__(self, name, courses):
        self._name = name
        self._courses = courses
    def get_name(self): return self._name
    def get_courses(self): return self._courses
class Class:
    def __init__(self, id, dept, course):
        self._id = id
        self._dept = dept
        self._course = course
        self._instructor = None
        self._meetingTime = None
        self._room = None
    def get_id(self): return self._id
    def get_dept(self): return self._dept
    def get_course(self): return self._course
    def get_instructor(self): return self._instructor
    def get_meetingTime(self): return self._meetingTime
    def get_room(self): return self._room
    def set_instructor(self, instructor): self._instructor = instructor
    def set_meetingTime(self, meetingTime): self._meetingTime = meetingTime
    def set_room(self, room): self._room = room
    def __str__(self): 
        return str(self._dept.get_name()) + "," + str(self._course.get_number()) + "," + str(self._room.get_number()) + "," + str(self._instructor.get_id()) + "," + str(self._meetingTime.get_id()+ " ")
class DisplayManager:
    def print_available_data(self):
        print("-- All Available Data --\n\n")
    def print_dept(self):
        print("-- All Available Departments with respective Courses --")
        depts= generate_schedule.data.get_depts()
        availableDeptsTable = prettytable.PrettyTable(['dept', 'courses'])
        for i in range(0, len(depts)):
            courses = depts.__getitem__(i).get_courses()
            tempStr = "["
            for j in range(0, len(courses)-1):
                tempStr += courses[j].__str__() + " , "
            tempStr += courses[len(courses)-1].__str__() + "]"
            availableDeptsTable.add_row([depts.__getitem__(i).get_name(), tempStr])
        print(availableDeptsTable)
    # def print_course(self):
    #     print("-- All Available Courses with respective Instructors --")
    #     courses = main_Data().get_courses()
    #     availableCoursesTable = prettytable.PrettyTable(['ID', 'Course', 'Max Number of Students', 'Instructors'])
    #     for i in range(0, len(courses)):
    #         instructors = courses[i].get_instructors()
    #         tempStr =""
    #         for j in range(0, len(instructors)-1):
    #             tempStr += instructors[j].__str__() +","
    #         tempStr += instructors[len(instructors)-1].__str__()
    #         availableCoursesTable.add_row(
    #             [courses[i].get_number(), courses[i].get_name(), str(courses[i].get_maxNumbOfStudents()), tempStr])
        # print(availableCoursesTable)
    def print_instructor(self):
        print("-- All Available Instructors--")
        availableInstructorsTable = prettytable.PrettyTable(['ID', 'Instructor'])
        instructors= main_Data().get_instructors()
        for i in range(0, len(instructors)):
            availableInstructorsTable.add_row([instructors[i].get_id(),instructors[i].get_name()])
        print(availableInstructorsTable)
        
    def print_room(self):
        print("-- All Available Rooms --")
        availableRoomsTable = prettytable.PrettyTable(['Room', 'Max Student Capacity'])
        rooms = main_Data().get_rooms()
        for i in range(len(rooms)):
            availableRoomsTable.add_row([str(rooms[i].get_number()), str(rooms[i].get_seatingCapacity())])
        print(availableRoomsTable)
        
    def print_meeting_times(self):
        print("-- All Available Meeting Time --")
        availableMeetingTimeTable = prettytable.PrettyTable(['Id','Day', 'Meeting Time'])
        meetingTimes= main_Data().get_meetingTimes()
        for i in range(0, len(meetingTimes)):
            availableMeetingTimeTable.add_row([meetingTimes[i].get_id(), meetingTimes[i].get_day(), meetingTimes[i].get_time()])
        print(availableMeetingTimeTable)
    def print_generation(self,population):
        table1= prettytable.PrettyTable(['Schdeule','Fitness','Conflicts','Classes[Dept,Course,Room,Instructor]'])
        schedules = population.get_schedules()
        for i in range(0, len(schedules)):
            table1.add_row([str(i),round(schedules[i].get_fitness(),3),schedules[i].get_numbOfConflicts(), schedules[i].__str__()])
        print(table1)
    def print_schedule_as_table(self,schedule):
        print("-- Schedule --")
        classes = schedule.get_classes()
        
        table= prettytable.PrettyTable(['Class','Dept', 'Course(number, max student)', 'Room(capacity)', 'Instructor', 'MeetingTime(id)' ])
        for i in range(0, len(classes)):
             table.add_row([str(i),classes[i].get_dept().get_name() ,classes[i].get_course().get_name() + "(" + 
                           str(classes[i].get_course().get_number()) + "," +
                           str(classes[i].get_course().get_maxNumbOfStudents()) + ")",
                           str(classes[i].get_room().get_number()) + "(" + str(classes[i].get_room().get_seatingCapacity()) + ")" , 
                           classes[i].get_instructor().get_name() + "(" + str(classes[i].get_instructor().get_id()) + ")",
                           classes[i].get_meetingTime().get_time()+ " " +classes[i].get_meetingTime().get_day() + " " + "(" + str(classes[i].get_meetingTime().get_id()) + ")"])
        # for i in range(0, len(data.get_depts())):
        #     print("-----" + data.get_depts()[i].get_name() +"------")
        #     table.add_row([str(i),classes[i].get_dept().get_name() ,classes[i].get_course().get_name() + "(" + 
        #                    classes[i].get_course().get_number() + "," +
        #                    str(classes[i].get_course().get_maxNumbOfStudents()) + ")",
        #                    classes[i].get_room().get_number() + "(" + str(classes[i].get_room().get_seatingCapacity()) + ")" , 
        #                    classes[i].get_instructor().get_name() + "(" + classes[i].get_instructor().get_id() + ")",
        #                    classes[i].get_meetingTime().get_time() + "(" + str(classes[i].get_meetingTime().get_id()) + ")"])
        print(table)

def main_Data():
    return Data();

def generate_schedule():
    # Data()
    # Schedule().initialize()
    displayMgr= DisplayManager()
    displayMgr.print_available_data()
    generationNumber= 0
    print("\nGeneration: " + str(generationNumber))
    population = Population(POPULATION_SIZE)
    population.get_schedules().sort(key=lambda x: x.get_fitness(),reverse=True)
    displayMgr.print_generation(population)
    displayMgr.print_schedule_as_table(population.get_schedules()[0])
    geneticAlgorithm = GeneticAlgorithm()
    schedule=[]
    while (population.get_schedules()[0].get_fitness() != 1):
        if(generationNumber==150):
            break
        generationNumber += 1
        print("\n> Generation # " + str(generationNumber))
        population = geneticAlgorithm.evolve(population)
        population.get_schedules().sort(key=lambda x: x.get_fitness(), reverse=True)
        displayMgr.print_generation(population)
        displayMgr.print_schedule_as_table(population.get_schedules()[0])
        schedule.append(population.get_schedules()[0])
    print("\n\n")
    print(len(schedule))
    return(schedule[len(schedule)-1])

# generate_schedule()