from schedulebuddy import db
from schedulebuddy.models import Course, User
import schedulebuddy.helpers as h
db.drop_all()
db.create_all()

# 0,1,2,3,4 = Fall, Winter, Spring, Summer1, Summer2

def TestFun():
    h.SetCourse(course_name="ECS150", units=4, difficulty=10, offered = [1,2,3], \
                prerequisites=[["ECS34","ECS36C","ECS60"], ["ECS154A","EEC170"]])
    h.SetCourse(course_name="ECS171", units=4, difficulty=7, offered = [1,2,3], \
                prerequisites=[["ECS60","ECS32B","ECS36C"]])
    h.SetCourse(course_name="ECS140", units=4, difficulty=6, offered = [1,2,4], \
                prerequisites=[["ECS50"],["ECS60","ECS32B","ECS36C"],["ECS20"],["ECS150"]])
    h.SetCourse(course_name="ECS122A", units=4, difficulty=9, offered = [3],\
        prerequisites=[["ECS20"], ["ECS60","ECS32B","ECS36C"]])
    h.SetCourse(course_name="ECS50", units=4, difficulty=5, offered = [3],\
        prerequisites=[["NAN"]])
    h.SetCourse(course_name="ECS36C", units=4, difficulty=6, offered = [3],\
        prerequisites=[["NAN"]])
    h.SetUser(first_name="bob", last_name="tom", graduation=2020, school="UC Davis", past_courses=["ECS50","ECS36C","ECS20"])
    
    print("course offered: ",Course.query.filter(Course.course_name == "ECS140")[0].offered)
    h.GetQuartersOffered("ECS140")
    print("This is the valid Couse list: ", h.GetValidRegList(1))
    UpdateDiffTest([1,2], [10,10])

    x = [[1,2,3],[1,2,3,4,5,6],[1]]
    print(len(x[1]))

def UpdateDiffTest(courses, difficulties):
    new_diff = h.UpdateDifficulty(courses, difficulties)
    print(new_diff)
    print([((10 * 100) + 10)/101, ((7*100) + 10) / 101])
    if(new_diff != [((10 * 100) + 10)/101, ((7*100) + 10) / 101]):
        print("UpdateDiffTest Pass")
    else:
        print("UpdateDiffTest Fail")
