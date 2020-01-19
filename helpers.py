def GetDifficultySum(courses):
    _sum = 0
    for course in courses:    
        _sum += Course.query.filter(Course.id == course)[0].difficulty
    return _sum

def SetCourse(course_name, units, difficulty, offered):
    course = Course(course_name=course_name, units=units, difficulty=difficulty, offered=offered)
    db.session.add(course)
    db.session.commit()


def SetUser(first_name, last_name, graduation, school, past_courses):
    user = User(first_name=first_name, last_name=last_name, graduation=graduation, school=school, past_courses=past_courses)
    db.session.add(user)
    db.session.commit()