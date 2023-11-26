import random
from Course import Course

class Schedule:
    def __init__(self, courseList, maxDays, maxBreaks, maxCourse):
        self.__schedule = courseList      
        self.__schedule.sort(key=lambda course: (course.get_days(), course.get_start_time()))   
        # convert these to int
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
   
        IDs = set([course.get_id() for course in self.__schedule])
        
        if len(IDs) != len(self.__schedule):
            return 0
                
        valid= [1]*len(self.__schedule)
        for  course in (self.__schedule):
            for otherCourse in (self.__schedule):
                ok = True
                if not ok:
                    break
                if course.get_id() != otherCourse.get_id() and valid[self.__schedule.index(course)] == 1 and valid[self.__schedule.index(otherCourse)] == 1:
                    for day in course.get_days():
                        if day in otherCourse.get_days() and course.get_start_time() <= otherCourse.get_end_time() and course.get_end_time() >= otherCourse.get_start_time():
                            rand = random.randint(0,1)
                            
                            valid[self.__schedule.index(otherCourse)] = 0
                            
        #extract invalid courseList
        newSchedule = []
        for i in range(len(valid)):
            if valid[i] == 1:
                newSchedule.append(self.__schedule[i])
        
        self.__schedule = newSchedule
        
        #that the days are not more than maxDays
        fitness = [0]*3
        weights = [.6,.2,.2]
        
        days= len(set([day for course in self.__schedule for day in course.get_days()]))
        
        
        fitness[0] = min(1,  days / self.__maxDays)
        
        
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
                     

        total_breaks_penalty = max(0, breaks - self.__maxBreaks)  # Calculate the penalty for exceeding maxBreaks
        fitness[1] = 1 / (1 + total_breaks_penalty) 
            
        #calculate that courses number are close to maxCourse as possible with strong equation
        courses = len(self.__schedule)
        fitness[2] = 1 / (1 + abs(self.__maxCourses - courses))
        
        #normalize 
        normalized_fitness = sum(f * w for f, w in zip(fitness, weights)) / sum(weights)
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

