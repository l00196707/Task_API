import logging
from flask import Flask, jsonify, Blueprint, request, current_app

tasks_bp = Blueprint("tasks", __name__, url_prefix="/tasks")

state = {
    "tasks": {
        1: {"id": 1, "title": "setup project", "completed": True},
        2: {"id": 2, "title": "add metrics", "completed": False},
        3: {"id": 3, "title": "configure logging", "completed": False},
    },
    "next_id": 4,
}


@tasks_bp.route("/", methods=["GET"], strict_slashes=False)
def list_tasks():
    """
    Return all tasks
    """
    return jsonify(list(state["tasks"].values())), 200


@tasks_bp.route("/<int:task_id>", methods=["GET"], strict_slashes=False)
def get_task(task_id):
    """
    Return a task by id
    """
    task = state["tasks"].get(task_id)

    if not task:
        current_app.logger.warning("Task not found: %s", task_id)
        return jsonify({"error": "task not found"}), 404

    return jsonify(task), 200


@tasks_bp.route("/", methods=["POST"], strict_slashes=False)
def create_task():
    """
    Create a new task
    """

    data = request.get_json()

    if not data or "title" not in data:
        current_app.logger.warning("Invalid task creation request")
        return jsonify({"error": "title is required"}), 400

    task = {"id": state["next_id"], "title": data["title"], "completed": False}

    state["tasks"][state["next_id"]] = task
    state["next_id"] += 1

    state["tasks"][state["next_id"]] = task
    state["next_id"] += 1

    current_app.logger.info("Task created: %s", task["id"])

    return jsonify(task), 201


@tasks_bp.route("/<int:task_id>", methods=["DELETE"], strict_slashes=False)
def delete_task(task_id):
    """
    Delete a task by ID
    """
    task = state["tasks"].pop(task_id, None)

    if not task:
        current_app.logger.warning("Delete failed, task not found: %s", task_id)
        return jsonify({"error": "task not found"}), 404

    current_app.logger.info("Task deleted: %s", task_id)

    return jsonify({"message": "task deleted"}), 200
