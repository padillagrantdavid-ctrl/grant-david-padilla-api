
import sqlite3
import os

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, 'students.db')


# Database connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


# Home page
@app.route('/')
def home():
    return render_template('index.html')


# Student information API
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "2026-00123",
        "name": "Grant David Padilla",
        "program": "BSIT",
        "year": 1,
        "section": "A"
    })


# Greeting API
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')

    return jsonify({
        "message": f"Hello, {name}!"
    })


# Hobbies API
@app.route('/my-hobbies')
def my_hobbies():
    return jsonify({
        "name": "Grant David Padilla",
        "hobbies": [
            "Playing billiards",
            "Playing online games",
            "Listening to music"
        ],
        "favorite_hobby": "Playing billiards"
    })


# Addition API
@app.route('/add')
def add_numbers():
    try:
        num1 = float(request.args.get('num1', 0))
        num2 = float(request.args.get('num2', 0))

        return jsonify({
            "number1": num1,
            "number2": num2,
            "sum": num1 + num2
        })

    except ValueError:
        return jsonify({
            "error": "Please enter valid numbers"
        }), 400


# Get all students
@app.route('/students')
def get_students():
    conn = get_db_connection()

    students = conn.execute(
        'SELECT * FROM students ORDER BY id'
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


# Get student by ID
@app.route('/students/<int:id>')
def get_student_by_id(id):
    conn = get_db_connection()

    student = conn.execute(
        'SELECT * FROM students WHERE id = ?',
        (id,)
    ).fetchone()

    conn.close()

    if student is None:
        return jsonify({
            "error": "Student not found"
        }), 404

    return jsonify(dict(student))


# Additional endpoint: Search by program
@app.route('/students/program/<program>')
def get_students_by_program(program):
    conn = get_db_connection()

    students = conn.execute(
        'SELECT * FROM students WHERE UPPER(program) = ? ORDER BY id',
        (program.upper(),)
    ).fetchall()

    conn.close()

    return jsonify([dict(student) for student in students])


if __name__ == '__main__':
    app.run(debug=True)
