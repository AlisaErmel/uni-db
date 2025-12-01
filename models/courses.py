from bson.objectid import ObjectId
from db import db

def get_all_courses():
    return list(db.courses.find())

def get_course(course_id):
    return db.courses.find_one({"_id": ObjectId(course_id)})

def add_course(name, teacher_name, credits, year, semester, topics):
    return db.courses.insert_one({
        "name": name,
        "teacher_name": teacher_name,
        "credits": credits,
        "year": year,
        "semester": semester,
        "topics": topics
    }).inserted_id

def update_course(course_id, data):
    db.courses.update_one({"_id": ObjectId(course_id)}, {"$set": data})

def delete_course(course_id):
    db.courses.delete_one({"_id": ObjectId(course_id)})
