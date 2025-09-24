from flask import Flask
import os
import dotenv

from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf import CSRFProtect

dotenv.load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()


def create_app():
    # --- App & Config ---
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.secret_key = os.environ.get("SECRET_KEY")
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///unidep.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # --- Init ---
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # --- Login Manager Config ---
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "info"
    login_manager.login_message = "Ushbu sahifani ko‘rish uchun tizimga kiring!"

    # --- User Loader ---
    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    # --- Register Blueprints ---
    from . import main, auth

    app.register_blueprint(main.bp, url_prefix="/")
    app.register_blueprint(auth.bp, url_prefix="/usr")

    return app
