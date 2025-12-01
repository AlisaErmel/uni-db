from bson.objectid import ObjectId
from db import db

def get_all_grades():
    return list(db.grades.find())

def add_grade(student_id, course_id, grade_value, comment):
    # validate references
    student = db.students.find_one({"_id": ObjectId(student_id)})
    course = db.courses.find_one({"_id": ObjectId(course_id)})
    if not student or not course:
        return None
    return db.grades.insert_one({
        "student_id": ObjectId(student_id),
        "course_id": ObjectId(course_id),
        "grade": grade_value,
        "comment": comment
    }).inserted_id

def update_grade(grade_id, data):
    db.grades.update_one({"_id": ObjectId(grade_id)}, {"$set": data})

def delete_grade(grade_id):
    db.grades.delete_one({"_id": ObjectId(grade_id)})
