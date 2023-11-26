
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
        #check if the time is in the format hh:mm and is string 
        if type(self.__start_time) == str and ":" in self.__start_time:
            m = int(self.__start_time[:2])*60 + int(self.__start_time[3:])
        else:
            m = int(self.__start_time)
        return m
    def get_end_time(self):
        if type(self.__end_time) == str and ":" in self.__end_time:
            m = int(self.__end_time[:2])*60 + int(self.__end_time[3:])
        else:
            m = int(self.__end_time)
        return  m
    def get_days(self):
        return self.__days
    def get_location(self):
        return self.__location
    
    