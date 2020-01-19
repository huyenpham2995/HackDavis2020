from app import db
from sqlalchemy.types import PickleType
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(20), unique=True, nullable=False)
    units = db.Column(db.Integer, nullable=False)
    offered = db.Column(PickleType, nullable=False)
    difficulty = db.Column(db.Integer, unique=False, nullable=False)
    times_taken = db.Column(db.Integer, nullable=False)
    prerequisites = db.Column(PickleType, nullable=False)


    def __repr__(self):
        return f"Course('{self.course_name}','{self.units}','{self.difficulty}','{self.offered}')"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=False)
    graduation = db.Column(db.Integer, nullable=True)
    school = db.Column(db.String(100), nullable=False)
    past_courses = db.Column(PickleType, nullable=False)
    def __repr__(self):
        return f"User('{self.first_name}','{self.last_name}','{self.graduation}','{self.school}','{self.past_courses}')"