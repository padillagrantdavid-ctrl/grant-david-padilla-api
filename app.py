
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my first API!"

@app.route('/student')
def get_student():
    return jsonify({
        "student_id": "24-00170",
        "name": "Grant David Padilla",
        "program": "BSIT",
        "year": 3,
        "section": "3B DIJKSTRA"
    })

@app.route('/hello')
def say_hello():
    name = request.args.get('name', 'Grant')
    return jsonify({
        "message": f"Hello, {name}!"
    })

if __name__ == '__main__':
    app.run(debug=True)
