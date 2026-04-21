from flask import Flask,jsonify,Blueprint,request

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

tasks = {
    1: {"id": 1, "title": "setup project", "completed": True},
    2: {"id": 2, "title": "add metrics", "completed": False},
    3: {"id": 3, "title": "configure logging", "completed": False}
}

next_id = 4

@tasks_bp.route("", methods=["GET"])
def list_tasks():
    """
    Return all tasks
    """
    return jsonify(list(tasks.values())), 200

@tasks_bp.route("/<int:task_id>", methods=["GET"])
def get_task(task_id):
    """
    Return a task by id
    """
    task = tasks.get(task_id)

    if not task:
        return jsonify({"error": "task not found"}), 404

    return jsonify(task), 200


@tasks_bp.route("", methods=["POST"])
def create_task():
    """
    Create a new task
    """
    global next_id

    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    task = {
        "id": next_id,
        "title": data["title"],
        "completed": False
    }

    tasks[next_id] = task
    next_id += 1

    return jsonify(task), 201

@tasks_bp.route("/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    """
    Delete a task by ID
    """
    task = tasks.pop(task_id,None)

    if not task:
        return jsonify({"error": "task not found"}), 404

    return jsonify({"message": "task deleted"}), 200
