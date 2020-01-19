from app import db
from Modules import Course, Offered, User
db.drop_all()
db.create_all()

# def AllCoursesOffered(courses, current_quarter):

#     for course in courses:
#         offered = False
#         for x in Offered.query.filter(Offered.course_id == course):
#             if x.quarter == current_quarter:
#                 offered = True
#                 break

    
def GetDifficultySum(courses):
    _sum = 0
    for course in courses:    
        _sum += Course.query.filter(Course.id == course)[0].difficulty
    return _sum

def SetCourse(course_name, units, difficulty, offered):
    course = Course(course_name=course_name, units=units, difficulty=difficulty, offered=offered)
    db.session.add(course)
    db.session.commit()

    # for quarter in offered:
    #     offering = Offered(quarter=quarter, course_id=course.id)
    #     db.session.add(offering)
    # db.session.commit()


def SetUser(first_name, last_name, graduation, school, past_courses):
    user = User(first_name=first_name, last_name=last_name, graduation=graduation, school=school, past_courses=past_courses)
    db.session.add(user)
    db.session.commit()

SetCourse(course_name="ECS150", units=4, difficulty=10, offered = [1,2,3])
SetCourse(course_name="ECS171", units=4, difficulty=7, offered = [1,2,3])
SetCourse(course_name="ECS140", units=4, difficulty=6, offered = [1,2,4])
SetCourse(course_name="ECS122A", units=4, difficulty=9, offered = [3])

SetUser(first_name="bob", last_name="tom", graduation=2020, school="UC Davis", past_courses=[1,2])
print(User.query.get(1).past_courses)
# for x in Offered.query.filter(Offered.course_id == Course.query.get(1).id):
#     print(x.quarter)


