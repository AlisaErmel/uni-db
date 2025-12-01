from flask import Flask, render_template, request, redirect, url_for
from models import students, courses, grades
from bson import ObjectId

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# ===== Students =====
@app.route('/students')
def list_students():
    all_students = students.get_all_students()
    return render_template("students.html", students=all_students)

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        number = request.form['student_number']
        email = request.form['email']
        students.add_student(name, int(number), email)
        return redirect(url_for('list_students'))
    return render_template("add_student.html")

# ===== Courses =====
@app.route('/courses')
def list_courses():
    all_courses = courses.get_all_courses()
    return render_template("courses.html", courses=all_courses)

@app.route('/courses/add', methods=['GET', 'POST'])
def add_course():
    if request.method == 'POST':
        name = request.form['name']
        teacher = request.form['teacher_name']
        credits = int(request.form['credits'])
        year = int(request.form['year'])
        semester = request.form['semester']
        
        # Get list of topics safely
        topics = request.form.getlist('topics[]')  # returns a list
        topics = [t.strip() for t in topics if t.strip()]  # remove empty strings
    
        courses.add_course(name, teacher, credits, year, semester, topics)
        return redirect(url_for('list_courses'))
    return render_template("add_course.html")

# ===== Grades =====
@app.route('/grades')
def list_grades():
    all_grades = grades.get_all_grades()
    # Populate student/course names
    for g in all_grades:
        g['student'] = students.get_student(g['student_id'])['name']
        g['course'] = courses.get_course(g['course_id'])['name']
    return render_template("grades.html", grades=all_grades)

@app.route('/grades/add', methods=['GET', 'POST'])
def add_grade():
    all_students = students.get_all_students()
    all_courses = courses.get_all_courses()
    if request.method == 'POST':
        student_id = ObjectId(request.form['student_id'])
        course_id = ObjectId(request.form['course_id'])
        grade_value = int(request.form['grade'])
        comment = request.form['comment']
        grades.add_grade(student_id, course_id, grade_value, comment)
        return redirect(url_for('list_grades'))
    return render_template("add_grade.html", students=all_students, courses=all_courses)

if __name__ == "__main__":
    app.run(debug=True)
