from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask API! - Prince Reniel"

@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "YOUR-STUDENT-ID",
        "name": "Prince Reniel",
        "program": "BSIT",
        "year": 1,
        "section": "A"
    })

@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Student')
    return jsonify({
        "message": f"Hello, {name}!"
    })

# NEW ENDPOINT 1
@app.route('/my-hobbies')
def my_hobbies():
    return jsonify({
        "name": "Prince Reniel",
        "hobbies": [
            "Playing billiards",
            "Playing online games",
            "Listening to music"
        ],
        "favorite_hobby": "Playing billiards"
    })

# NEW ENDPOINT 2
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
        return jsonify({"error": "Please enter valid numbers"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)