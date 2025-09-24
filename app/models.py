from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from enum import Enum


class UserRole(Enum):
    TEACHER = "teacher"
    STUDENT = "student"
    ADMIN = "admin"


# --- User Model ---
class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.Enum(UserRole), nullable=False, default=UserRole.STUDENT)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    posts = db.relationship("Post", backref="author", lazy=True)

    def __repr__(self):
        return f"<User {self.email} | {self.role}>"


class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Post {self.title[:10]}... | {self.content[:10]}... >"
