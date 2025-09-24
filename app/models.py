from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from enum import Enum

class UserRole(Enum):
    TEACHER = 'teacher'
    STUDENT = 'student'
    ADMIN = 'admin'

# --- User Model ---
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.STUDENT)
    created_at = db.Column(db.DateTime, default=func.now())

    def __repr__(self):
        return f'<User {self.email} | {self.role}>'

