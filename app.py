from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration
users = {}
tasks = []

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data['username']
    password = data['password']
    if username in users:
        return jsonify({"message": "User already exists"}), 400
    users[username] = password
    return jsonify({"message": "User registered successfully"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    if users.get(username) == password:
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    task = data['task']
    deadline = data['deadline']
    tasks.append({"task": task, "deadline": deadline})
    return jsonify({"message": "Task added successfully"}), 200

@app.route('/delete_task/<int:index>', methods=['DELETE'])
def delete_task(index):
    if index < len(tasks):
        tasks.pop(index)
        return jsonify({"message": "Task deleted successfully"}), 200
    return jsonify({"message": "Invalid index"}), 400

if __name__ == '__main__':
    app.run(debug=True)
