from app import db
from Modules import Course, User
db.drop_all()
db.create_all()

SetCourse(course_name="ECS150", units=4, difficulty=10, offered = [1,2,3])
SetCourse(course_name="ECS171", units=4, difficulty=7, offered = [1,2,3])
SetCourse(course_name="ECS140", units=4, difficulty=6, offered = [1,2,4])
SetCourse(course_name="ECS122A", units=4, difficulty=9, offered = [3])

SetUser(first_name="bob", last_name="tom", graduation=2020, school="UC Davis", past_courses=[1,2])
print(User.query.get(1).past_courses)
print(Course.query.get(1).offered)
# for x in Offered.query.filter(Offered.course_id == Course.query.get(1).id):
#     print(x.quarter)


