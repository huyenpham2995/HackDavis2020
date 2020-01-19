from schedulebuddy import db
from schedulebuddy.models import Course, User

def GetDifficultySum(courses):
    _sum = 0
    for course in courses:    
        _sum += Course.query.filter(Course.id == course)[0].difficulty
    return _sum

def SetCourse(course_name, units, difficulty, offered, prerequisites, times_taken=100):
    course = Course(course_name=course_name, units=units, difficulty=difficulty, offered=offered,\
        prerequisites=prerequisites, times_taken=times_taken)
    db.session.add(course)
    db.session.commit()

def SetUser(first_name, last_name, graduation, school, past_courses):
    user = User(first_name=first_name, last_name=last_name, graduation=graduation, school=school,\
        past_courses=past_courses)
    db.session.add(user)
    db.session.commit()

def IncrementTimesTaken(course_id):
    Course.query.filter(Course.id == course_id)[0].times_taken += 1

def UpdateDifficulty(courses, difficulties):
    new_diff = []
    for course, difficulty in zip(courses, difficulties):
        old_diff = Course.query.filter(Course.id == course)[0].difficulty
        n = Course.query.filter(Course.id == course)[0].times_taken

        Course.query.filter(Course.id == course)[0].difficulty = ((n * old_diff) + difficulty) / (n + 1)
        new_diff.append(Course.query.filter(Course.id == course)[0].difficulty)
        IncrementTimesTaken(course) 
    return new_diff

def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    if (a_set & b_set): 
        return True 
    else: 
        return False

def GetValidRegList(user):
    past_courses = User.query.filter(User.id == user)[0].past_courses

    # List of courses that oune can register for
    valid_reg_list = []

    for course in Course.query.all():
        prereks = course.prerequisites
        
        is_course_taken = []
        for i in range(0,len(prereks)):
            is_course_taken.append(common_member(prereks[i], past_courses))
        if all(is_course_taken):
            valid_reg_list.append(course)
    return valid_reg_list
            
def GetQuartersOffered(course):
    print("$$$$$$$: ", Course.query.filter(Course.course_name == course)[0].offered)

# def GetCurrQuarterCourses(IQuarter):
#     LCourseList = []
#     for course in Course.query.all():
#         if common_member([IQuarter], )