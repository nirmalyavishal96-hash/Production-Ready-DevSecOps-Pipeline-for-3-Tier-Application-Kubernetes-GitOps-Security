from flask import Blueprint, request, render_template, jsonify, g, Response

from app.utils.auth import generate_token, requires_auth
from app.models.models import User, Task
from app import db

#  Prometheus
from prometheus_client import Counter, Gauge, generate_latest
import psutil

bp = Blueprint("main", __name__)

#  Metrics
REQUEST_COUNT = Counter('request_count', 'Total Requests')
CPU_USAGE = Gauge('cpu_usage_percent', 'CPU usage percent')


#  ROUTES 

@bp.route('/', methods=['GET'])
def index():
    REQUEST_COUNT.inc()
    return render_template('index.html')


@bp.route("/api/health", methods=["GET"])
def health_check():
    REQUEST_COUNT.inc()
    return jsonify({"status": "ok", "message": "Flask backend running smoothly!"})


@bp.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    REQUEST_COUNT.inc()
    return render_template('index.html')


#  USER 

@bp.route("/api/create_user", methods=["POST"])
def create_user():
    REQUEST_COUNT.inc()
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
    REQUEST_COUNT.inc()
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


#  TASKS 

@bp.route("/api/submit_task", methods=["POST"])
@requires_auth
def submit_task():
    REQUEST_COUNT.inc()

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
    REQUEST_COUNT.inc()

    return jsonify(
        tasks=[
            i.serialize for i in Task.get_tasks_for_user(g.current_user["id"]).all()
        ]
    )


@bp.route("/api/delete_task", methods=["POST"])
@requires_auth
def delete_task():
    REQUEST_COUNT.inc()

    incoming = request.get_json()

    success = Task.delete_task(incoming.get('task_id'))

    if not success:
        return jsonify(message="Error deleting task"), 409

    return jsonify(success=True)


#  METRICS 

@bp.route("/metrics")
def metrics():
    CPU_USAGE.set(psutil.cpu_percent())   
    return Response(generate_latest(), mimetype="text/plain")