import random
from Course import Course
from Schedule import Schedule

MUTATION_RATE = 0.02
POPULATION_SIZE = 100

class GA:
    def __init__(self,schedule,GenNum,maxDays, maxBreaks, maxCourses):
        self.maxDays = int(maxDays)
        self.maxBreaks = int(maxBreaks)
        self.maxCourses = int(maxCourses)
        self.populationSize = POPULATION_SIZE 
        self.mutationRate = MUTATION_RATE
        self.__Population = []
        self.__Population.append(schedule)

        self.__Population = self.initializePopulation()
 
        self.Generation =0 

        for i in range(GenNum):
            self.DoGeneration()
        
    def getBestSchedules(self,num):
        return self.__Population[:num]    
    def initializePopulation(self):
        
        population = self.__Population
        for i in range(0, self.populationSize):
            
            rand = random.randint(1,max(1, 2**(self.populationSize )-1))
            courses = self.__Population[0].get_schedule()
            newCourses = []
            for j in range(len(courses)):
                if rand & (1 << j):
                    newCourses.append(courses[j])
            population.append(Schedule(newCourses, self.maxDays, self.maxBreaks, self.maxCourses))
        
        return population
        
    def DoGeneration(self):
        offSpring = []
        for i in range(self.populationSize//2):
            mother = self.GetParent()
            father = self.GetParent()
            
            while mother == father:
                father = self.GetParent()   
            
            child1, child2 = self.crossover(mother, father), self.crossover(father, mother)
            child1, child2 = self.mutate(child1), self.mutate(child2)
            
            offSpring.append(child1)
            offSpring.append(child2)
           

        self.__Population += offSpring
        self.__Population.sort(key=lambda x: x.get_fitness() if x else 0, reverse=True)
        self.__Population = self.__Population[:self.populationSize]
        self.Generation += 1
                
        #print("Generation: ", self.Generation, " Fitness: ", self.__Population[0].get_fitness())
        
    def crossover(self, mother, father):
        if len(mother.get_schedule()) < 2 or len(father.get_schedule()) < 2:
            return Schedule(mother.get_schedule()+father.get_schedule(), self.maxDays, self.maxBreaks, self.maxCourses)
        rand1 = random.randint(1, max(1,len(mother.get_schedule()) - 1))
        tempSchedule = mother.get_schedule()[:rand1]
        appeard = set([course.get_id() for course in tempSchedule])
    
        for i in range(rand1, len(father.get_schedule()) ):
            if father.get_schedule()[i].get_id() not in appeard:
                tempSchedule.append(father.get_schedule()[i])
                appeard.add(father.get_schedule()[i].get_id())

        sch = Schedule(tempSchedule, self.maxDays, self.maxBreaks, self.maxCourses)
        sch.get_fitness()
        return sch

    def mutate(self, child):
        rand = random.uniform(0,1)
        temp = child.get_schedule()
        if rand < self.mutationRate:
            rand1 = random.randint(0, max(1,len(child.get_schedule()) - 1))
            if len(child.get_schedule()) - 1 > self.maxCourses:
                temp.pop(rand1)
        child.set_schedule(temp)
        return child
    
   
    def GetParent(self):
        rand = random.uniform(0,1)
        if rand < 0.5:
            return self.tournamentSelection()
        else:
            return self.biasedRandomSelection()
        
    def biasedRandomSelection(self):
        sm = sum([x.get_fitness() for x in self.__Population])
        if sm == 0:
            return self.tournamentSelection()
        prob = [x.get_fitness()/sm for x in self.__Population]
        probSum = sum(prob)
        normProb = [x/probSum for x in prob]
        
        cumulatedProb = [0]*len(normProb)
        tot = 0
        for i in range(len(normProb)):
            tot += normProb[i]
            cumulatedProb[i] = tot
        
        selected = random.uniform(0,1)
        
        for i in range(len(cumulatedProb)):
            if selected <= cumulatedProb[i]:
                return self.__Population[i]
        
        return self.__Population[len(self.__Population) - 1]
    def tournamentSelection(self):
        candidateA = random.randint(0, self.populationSize - 1)
        candidateB = random.randint(0, self.populationSize - 1)
        while candidateA == candidateB:
            candidateB = random.randint(0, self.populationSize - 1)
        
        #Tournament Selection
        if self.__Population[candidateA].get_fitness() > self.__Population[candidateB].get_fitness():
            return self.__Population[candidateA]
        else:
            return self.__Population[candidateB]
    
    
    
# courseList = [

#     Course(1, "Math", 8, 9, [1, 3, 5], "Room 1"),
#     Course(2, "English", 9, 10, [1, 3, 5], "Room 2"),
#     Course(3, "Physics", 10, 11, [1, 3, 5], "Room 3"),
#     Course(4, "Chemistry", 11, 12, [1, 3, 5], "Room 4"),
#     Course(5, "History", 12, 13, [1, 3, 5], "Room 5"),
#     Course(6, "Geography", 13, 14, [1, 3, 5], "Room 6"),
#     Course(7, "Biology", 14, 15, [1, 3, 5], "Room 7"),
#     Course(8, "Computer Science", 15, 16, [1, 3, 5], "Room 8"),
#     Course(9, "Spanish", 16, 17, [1, 3, 5], "Room 9"),
# ]
# sch = Schedule(courseList,3, 0,7)

# ga = GA(sch,10,3, 60,7)

# schedule = ga.getBestSchedules(1)[0]
 
# for course in schedule.get_schedule():
#     print(course.get_name(), course.get_days(), course.get_start_time(), course.get_end_time(), course.get_location())

# print(schedule.get_fitness())

