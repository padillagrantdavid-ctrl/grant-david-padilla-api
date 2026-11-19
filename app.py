
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# STUDENT INFORMATION API
@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "YOUR-STUDENT-ID",
        "name": "Grant David Padilla",
        "program": "BSIT",
        "year": 1,
        "section": "A"
    })


# GREETING API
@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')

    return jsonify({
        "message": f"Hello, {name}!"
    })


# MY HOBBIES API
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


# ADD NUMBERS API
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


if __name__ == '__main__':
    app.run(debug=True)
