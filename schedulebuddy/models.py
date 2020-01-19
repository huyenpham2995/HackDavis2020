from schedulebuddy import db

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(20), unique=True, nullable=False)
    units = db.Column(db.Integer, nullable=False)
    offered = db.relationship('Offered', backref='author', lazy=True)
    difficulty = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return f"Course('course_name: {self.course_name}','units: {self.units}','difficulty: {self.difficulty}','offered:{self.offered}')"

class Offered(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quarter = db.Column(db.Integer, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    def __repr__(self):
        return f"Offered('{self.quarter}')"
