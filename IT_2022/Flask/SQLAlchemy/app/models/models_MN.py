from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

enrollment = db.Table(
    "enrollment",
    db.Column("student_id", db.Integer, db.ForeignKey("student.id"), primary_key=True),
    db.Column("course_id", db.Integer, db.ForeignKey("course.id"), primary_key=True),
)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    courses = db.relationship("Course", secondary=enrollment, back_populates="students")


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    students = db.relationship(
        "Student", secondary=enrollment, back_populates="courses"
    )
