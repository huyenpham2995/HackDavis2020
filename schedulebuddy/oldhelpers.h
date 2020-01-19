from app import db
from Modules import Course, User

def GetDifficultySum(courses):
    _sum = 0
    for course in courses:    
        _sum += Course.query.filter(Course.id == course)[0].difficulty
    return _sum

def SetCourse(course_name, units, difficulty, offered, prerequisites,times_taken=100):
    course = Course(course_name=course_name, units=units, difficulty=difficulty, \
        offered=offered, prerequisites=prerequisites, times_taken=times_taken)
    db.session.add(course)
    db.session.commit()


def SetUser(first_name, last_name, graduation, school, past_courses):
    user = User(first_name=first_name, last_name=last_name, graduation=graduation, \
        school=school, past_courses=past_courses)
    db.session.add(user)
    db.session.commit()

def InclTimesTaken(course_id):
    Course.query.filter(Course.id == course_id)[0].times_taken += 1
    print("times talen = ", Course.query.filter(Course.id == course_id)[0].times_taken)

def UpdateDifficulty(courses, difficulties):
    new_diff = []
    for course, difficulty in zip(courses, difficulties):
        # print("course", course)
        # print("difficulty", difficulty)
        # print("for: ",new_diff)
        old_diff = Course.query.filter(Course.id == course)[0].difficulty
        n = Course.query.filter(Course.id == course)[0].times_taken
        
        Course.query.filter(Course.id == course)[0].difficulty = ((n * old_diff) + difficulty) / (n + 1)
        new_diff.append(Course.query.filter(Course.id == course)[0].difficulty)
        InclTimesTaken(course) 
        # print("new Diff: ", new_diff)
    return new_diff