from bson.objectid import ObjectId
from db import db

def get_all_students():
    return list(db.students.find())

def get_student(student_id):
    return db.students.find_one({"_id": ObjectId(student_id)})

def add_student(name, student_number, email):
    return db.students.insert_one({
        "name": name,
        "student_number": student_number,
        "email": email
    }).inserted_id

def update_student(student_id, data):
    db.students.update_one({"_id": ObjectId(student_id)}, {"$set": data})

def delete_student(student_id):
    db.students.delete_one({"_id": ObjectId(student_id)})
