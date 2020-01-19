from schedulebuddy import db
from schedulebuddy.models import Course, Offered
import helpers as h

db.drop_all()
db.create_all()

# 0,1,2,3,4 = Fall, Winter, Spering, Summer1, Summer2

h.SetCourse(course_name="ECS150", units=4, difficulty=10, offered = [1,2,3])
h.SetCourse(course_name="ECS171", units=4, difficulty=7, offered = [1,2,3])
h.SetCourse(course_name="ECS140", units=4, difficulty=6, offered = [1,2,4])
h.SetCourse(course_name="ECS122A", units=4, difficulty=9, offered = [3])

h.SetUser(first_name="bob", last_name="tom", graduation=2020, school="UC Davis", past_courses=[1,2])
#print(User.query.get(1).past_courses)
#print(Course.query.get(1).offered)
# for x in Offered.query.filter(Offered.course_id == Course.query.get(1).id):
#     print(x.quarter)

def getQuarters(course):
    arr = []
    for x in Offered.query.filter(Offered.course_id == Course.query.get(3).id):
        arr.append(x.quarter)
    return arr

def UpdateDiffTest(courses, difficulties):
    new_diff = h.UpdateDifficulty(courses, difficulties)
    print(new_diff)
    print([((10 * 100) + 10)/101, ((7*100) + 10) / 101])
    if(new_diff != [((10 * 100) + 10)/101, ((7*100) + 10) / 101]):
        print("UpdateDiffTest Pass")
    else:
        print("UpdateDiffTest Fail")

UpdateDiffTest([1,2], [10,10])

x = [[1,2,3],[1,2,3,4,5,6],[1]]
print(len(x[1]))
