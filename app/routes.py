from flask import Blueprint, request, render_template, jsonify, g

from app.utils.auth import generate_token, requires_auth
from app.models.models import User, Task
from app import db

# Create Blueprint
bp = Blueprint("main", __name__)

# ------------------ ROUTES ------------------

@bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@bp.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "Flask backend running smoothly!"})


@bp.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')


# ------------------ USER ------------------

@bp.route("/api/create_user", methods=["POST"])
def create_user():
    incoming = request.get_json()
    
    success = User.create_user(incoming)

    if not success:
        return jsonify(message="User with that email already exists"), 409

    new_user = User.query.filter_by(email=incoming["email"]).first()

    return jsonify(
        id=new_user.id,
        token=generate_token(new_user.id)
    )


@bp.route("/api/get_token", methods=["POST"])
def get_token():
    incoming = request.get_json()
    user = User.get_user_with_email_and_password(
        incoming["email"],
        incoming["password"]
    )

    if user:
        return jsonify(
            token=generate_token(user.id),
            user_id=user.id   
        )

    return jsonify(error=True), 403


# ------------------ TASKS ------------------

@bp.route("/api/submit_task", methods=["POST"])
@requires_auth
def submit_task():
    incoming = request.get_json()

    success, task_id = Task.add_task(
        incoming.get("task"),
        g.current_user["id"],
        incoming.get("status")
    )

    if not success:
        return jsonify(message="Error submitting task", id=None), 409

    return jsonify(success=True, id=task_id)


@bp.route("/api/get_tasks_for_user", methods=["POST"])
@requires_auth
def get_tasks_for_user():
    return jsonify(
        tasks=[
            i.serialize for i in Task.get_tasks_for_user(g.current_user["id"]).all()
        ]
    )


@bp.route("/api/delete_task", methods=["POST"])
@requires_auth
def delete_task():
    incoming = request.get_json()

    success = Task.delete_task(incoming.get('task_id'))

    if not success:
        return jsonify(message="Error deleting task"), 409

    return jsonify(success=True)