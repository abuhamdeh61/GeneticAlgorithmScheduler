
class Course:
    def __init__(self,id,name,start_time,end_time,days,location):
        self.__id = id
        self.__name = name
        self.__start_time = start_time
        self.__end_time = end_time
        self.__days = days
        self.__location = location
    
    #getters 
    def get_id(self):
        return self.__id
    def get_name(self):
        return self.__name
    def get_start_time(self):
        #convert 00:00 to minutes
        m = int(self.__start_time[:2])*60 + int(self.__start_time[3:])
        return m
    def get_end_time(self):
        m = int(self.__end_time[:2])*60 + int(self.__end_time[3:])
        return  m
    def get_days(self):
        return self.__days
    def get_location(self):
        return self.__location
    
    