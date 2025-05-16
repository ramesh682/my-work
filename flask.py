from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask!"

@app.route('/api/data', methods=['GET'])
def get_data():
    sample_data = {"name": "Ramesh", "role": "Full Stack Developer"}
    return jsonify(sample_data)

@app.route('/greet/<username>')
def greet_user(username):
    return f"Hello, {username}!"

if __name__ == '__main__':
    app.run(debug=True)
