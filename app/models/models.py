from datetime import datetime
from sqlalchemy.exc import IntegrityError
from app import db, bcrypt


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = self.hash_password(password)

    #  HASH PASSWORD
    @staticmethod
    def hash_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    #  CREATE USER
    @staticmethod
    def create_user(payload):
        user = User(
            email=payload["email"],
            password=payload["password"],
            first_name=payload["first_name"],
            last_name=payload["last_name"],
        )

        try:
            db.session.add(user)
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    #  GET USER BY ID
    @staticmethod
    def get_user_by_id(user_id):
        return User.query.filter_by(id=user_id).first()

    #  LOGIN 
    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            return user

        return None


class Task(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.DateTime())
    task = db.Column(db.String(255))
    user_id = db.Column(db.Integer)   # FIXED TYPE 
    status = db.Column(db.String(255))

    def __init__(self, task, user_id, status):
        self.date = datetime.utcnow()
        self.task = task
        self.user_id = user_id
        self.status = status

    #  ADD TASK
    @staticmethod
    def add_task(task, user_id, status):
        new_task = Task(
            task=task,
            user_id=user_id,
            status=status
        )

        db.session.add(new_task)

        try:
            db.session.commit()
            return True, new_task.id
        except IntegrityError:
            db.session.rollback()
            return False, None

    #  GET TASKS FOR USER
    @staticmethod
    def get_tasks_for_user(user_id):
        return Task.query.filter_by(user_id=user_id)

    #  DELETE TASK
    @staticmethod
    def delete_task(task_id):
        task = Task.query.filter_by(id=task_id).first()

        if not task:
            return False

        db.session.delete(task)

        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    # EDIT TASK
    @staticmethod
    def edit_task(task_id, task, status):
        task_to_edit = Task.query.filter_by(id=task_id).first()

        if not task_to_edit:
            return False

        task_to_edit.task = task
        task_to_edit.status = status

        try:
            db.session.commit()
            return True
        except IntegrityError:
            db.session.rollback()
            return False

    # SERIALIZER
    @property
    def serialize(self):
        return {
            'id': self.id,
            'date': self.date.strftime("%Y-%m-%d"),
            'task': self.task,
            'user_id': self.user_id,
            'status': self.status,
        }