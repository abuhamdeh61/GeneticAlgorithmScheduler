import json
from flask import Flask, render_template, request, redirect, url_for, flash
from Schedule import Schedule
from GA import GA
from Course import Course
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule',methods=['GET','POST'])
def schedule():
    
    if request.method == 'POST':
        try:    
            data = request.get_json()
            for d in data:
                #check if there's something missing
                for key in d:
                    if key == None :
                        return json.dumps({'status':'error','error':'missing field'})
            
            courseList = []
            for d in data:
                if len(d) > 2:
                    
                    days = []
                    for day in d[4]:
                        if type(day) == int:
                            days.append(day)
                            continue
                        day = day.strip().lower()[:2]
                        if day == 'su':
                            days.append(1)
                        elif day == 'mo':
                            days.append(2)
                        elif day == 'tu':
                            days.append(3)
                        elif day == 'we':
                            days.append(4)
                        elif day == 'th':
                            days.append(5)
                        elif day == 'fr':
                            days.append(6)
                        elif day == 'sa':
                            days.append(7)
                    courseList.append(Course(d[0],d[1],d[2],d[3],days,d[5]))

            maxDays = data[len(data)-1][1]
            maxBreaks = data[len(data)-2][1]
            maxCourses = data[len(data)-3][1]
            
            schedule = Schedule(courseList,maxDays,maxBreaks,maxCourses)
            ga = GA(schedule,50,maxDays,maxBreaks,maxCourses)
            schedule = ga.getBestSchedules(1)[0].get_schedule()
            data = [[]]
            
            for course in schedule:
                data[0].append({'id':course.get_id(),'name':course.get_name(),'start_time':course.get_start_time(),'end_time':course.get_end_time(),'days':course.get_days(),'location':course.get_location()})
            
            return json.dumps({'status':'success','data':data})
        
        except Exception as e:
            print(e)
            return json.dumps({'status':'error','error':str(e)+"line "+str(e.__traceback__.tb_lineno)})
    

    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
