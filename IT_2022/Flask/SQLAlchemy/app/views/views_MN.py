from faker import Faker
from flask import jsonify, redirect, render_template, url_for

from app import app, db

from ..models.models_MN import Course, Student

faker = Faker()


@app.route("/generate_data_MN")
def generate_data_MN():
    student = Student(name=faker.name())
    db.session.add(student)
    db.session.commit()

    course1 = Course(title=faker.word())
    course2 = Course(title=faker.word())
    db.session.add(course1)
    db.session.add(course2)
    db.session.commit()

    student.courses.append(course1)
    student.courses.append(course2)
    course1.students.append(student)
    course2.students.append(student)
    db.session.commit()

    return jsonify(
        {
            "student": student.name,
            "courses": [course.title for course in student.courses],
        }
    )


@app.route("/select_data_MN")
def select_data_MN():
    students = Student.query.all()
    courses = Course.query.all()

    return jsonify(
        {
            "students": [
                {
                    "student": student.name,
                    "courses": [course.title for course in student.courses],
                }
                for student in students
            ],
            "courses": [
                {
                    "course": course.title,
                    "students": [student.name for student in course.students],
                }
                for course in courses
            ],
        }
    )


@app.route("/delete_data_MN")
def delete_data_MN():
    student = Student.query.first()
    db.session.delete(student)
    db.session.commit()
    return jsonify(student.name if student else None)
