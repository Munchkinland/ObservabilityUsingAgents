from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"message": "Hello from Flask!"})

@app.route('/heavy-task')
def heavy_task():
    time.sleep(random.uniform(1, 5))  # Simula una tarea pesada
    return jsonify({"message": "Task completed!"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
