import random
from Course import Course

class Schedule:
    def __init__(self, courseList, maxDays, maxBreaks, maxCourse):
        self.__schedule = courseList      
        self.__schedule.sort(key=lambda course: (course.get_days(), course.get_start_time()))   
        self.__maxDays = int(maxDays)
        self.__maxBreaks = int(maxBreaks)
        self.__maxCourses = int(maxCourse)
        self.__fitness = self.getNormalizedFitness()
    
    def set_schedule(self, schedule):
        self.__schedule = schedule
        self.__fitness = self.getNormalizedFitness()
        
    def get_fitness(self):
        return self.__fitness
    def get_schedule(self):
        return self.__schedule
    def getNormalizedFitness(self) :
                
        valid= [1]*len(self.__schedule)
        for i in range(len(self.__schedule)):
            course = self.__schedule[i]
            ok  = 1 
            for j in range(i+1,len(self.__schedule)):
                otherCourse = self.__schedule[j]
                if valid[self.__schedule.index(otherCourse)] == 0  :
                    continue
                if course.get_id() == otherCourse.get_id():
                    rand = random.randint(0,1)
                    if rand == 0:
                        valid[self.__schedule.index(course)] = 0
                        ok = 0
                        break
                    else:
                        valid[self.__schedule.index(otherCourse)] = 0
                        continue
                
                for day in course.get_days():
                    if day in otherCourse.get_days():
                        if course.get_start_time() >= otherCourse.get_start_time() and course.get_end_time() > otherCourse.get_start_time():
                            rand = random.randint(0,1)
                            if rand == 0:
                                valid[self.__schedule.index(course)] = 0
                                ok = 0
                                break
                            else:
                                valid[self.__schedule.index(otherCourse)] = 0
                                ok = -1 
                                break
                    if ok == -1:
                        break
                if ok == 0:
                    break
                
            with open('log.txt','a') as f:
                for i in valid:
                    f.write(str(i)+" ")
                f.write("\n")
        #extract invalid courseList
        newSchedule = []
        for i in range(len(valid)):
            if valid[i] == 1:
                newSchedule.append(self.__schedule[i])
        
        self.__schedule = newSchedule
        
        fitness = [0]*3
        weights = [30,30,100]
        
        days= len(set([day for course in self.__schedule for day in course.get_days()]))
        
        
        #calc fitness for days with strong math function that the penalty will be high if the days are more than maxDays and more higher if the days are less than maxDays
        days = self.__maxDays - days
        fitness[0] = 1 / (abs(days)*(1 if days <=0 else 2 )+ 1)
        
        
        #calculate the breaks between only the valid courseList
        breaks = 0 

        for day in range(1,7):

            for i in range(len(self.__schedule)):
                if day in self.__schedule[i].get_days():
                    if i == len(self.__schedule)-1:
                        break
                    elif day in self.__schedule[i+1].get_days():
                        if self.__schedule[i].get_end_time() != self.__schedule[i+1].get_start_time():
                            breaks += self.__schedule[i+1].get_start_time() - self.__schedule[i].get_end_time()
                     

        breaks = abs(breaks - self.__maxBreaks ) # Calculate the penalty for exceeding maxBreaks
        fitness[1] = 1 / (1 + (breaks if breaks <=self.__maxBreaks else self.__maxBreaks * 2)) 
            
        courses = len(self.__schedule)
        courses = courses - self.__maxCourses 
        fitness[2] = 1 / (abs(courses) * (0 if courses >= 0 else 10)+ 1)
        

        normalized_fitness = 0
        
        for i in range(len(fitness)):
            normalized_fitness += fitness[i] * weights[i]
            
        return normalized_fitness


# courses = [
#     Course(763501, 60, "13:00", "14:00", ['MO', 'WE'], "Location 1"),
#     Course(561181, 60, "16:00", "17:00", ['SU', 'TU', 'TH'], "Location 2"),
#     Course(101121, 60, "09:00", "10:00", ['MO', 'WE'], "Location 3"),
#     Course(159661, 60, "18:00", "19:00", ['MO', 'WE'], "Location 4"),
#     Course(92861, 60, "11:00", "12:00", ['SU', 'TU', 'TH'], "Location 5"),
#     Course(814411, 60, "15:00", "16:00", ['SU', 'TU', 'TH'], "Location 6"),
#     Course(848181, 60, "13:00", "14:00", ['MO', 'WE'], "Location 7"),
#     Course(41981, 60, "15:00", "16:00", ['MO', 'TH'], "Location 8"),
#     Course(556371, 60, "12:00", "13:00", ['SU', 'TU', 'TH'], "Location 9"),
#     Course(886041, 60, "11:00", "12:00", ['SU', 'TU', 'TH'], "Location 10"),
#     Course(97631, 60, "17:00", "18:00", ['SU', 'TU', 'TH'], "Location 11"),
#     Course(219241, 60, "18:00", "19:00", ['SU', 'TU', 'TH'], "Location 12"),
#     Course(564201, 60, "17:00", "18:00", ['SU', 'TU', 'TH'], "Location 13"),
#     Course(873291, 60, "09:00", "10:00", ['SU', 'TU', 'TH'], "Location 14"),
#     Course(75571, 60, "09:00", "10:00", ['MO', 'WE'], "Location 15"),
#     Course(365531, 60, "17:00", "18:00", ['SU', 'TU', 'TH'], "Location 16"),
#     Course(401551, 60, "08:00", "09:00", ['SU', 'TU', 'TH'], "Location 17"),
#     Course(541211, 60, "13:00", "14:00", ['SU', 'TU', 'TH'], "Location 18"),
#     Course(947501, 60, "18:00", "19:00", ['SU', 'TU', 'TH'], "Location 19"),
#     Course(413061, 60, "12:00", "13:00", ['SU', 'TU', 'TH'], "Location 20"),
#     Course(317051, 60, "15:00", "16:00", ['SU', 'TU', 'TH'], "Location 21"),
#     Course(208751, 60, "18:00", "19:00", ['MO', 'WE'], "Location 22"),
#     Course(35101, 60, "17:00", "18:00", ['SU', 'TU', 'TH'], "Location 23"),
#     Course(518731, 60, "09:00", "10:00", ['MO', 'TH'], "Location 24"),
#     Course(47031, 60, "08:00", "09:00", ['SU', 'TU', 'TH'], "Location 25"),
#     Course(452911, 60, "13:00", "14:00", ['SU', 'TU', 'TH'], "Location 26"),
#     Course(111201, 60, "13:00", "14:00", ['SU', 'TU', 'TH'], "Location 27"),
#     Course(53011, 60, "13:00", "14:00", ['SU', 'TU', 'TH'], "Location 28"),
#     Course(331601, 60, "18:00", "19:00", ['MO', 'WE'], "Location 29"),
#     Course(400741, 60, "13:00", "14:00", ['MO', 'WE'], "Location 30")
# ]



# sch = Schedule(courses, 3, 0, 7)
# print(sch.get_fitness())
# for course in sch.get_schedule():
#     print(course.get_id(), course.get_days(), course.get_start_time(), course.get_end_time(), course.get_location())