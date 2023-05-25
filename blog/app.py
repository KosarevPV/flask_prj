import os

from flask import Flask
from dotenv import load_dotenv
from flask_migrate import Migrate

from blog.user.views import user
from blog.post.views import post
from blog.authors.views import authors
from blog.auth.views import auth, login_manager
from blog.models.database import db
from blog.admin import admin


def create_app() -> Flask:
    app = Flask(__name__)

    migrate = Migrate(app, db, compare_type=True)

    load_dotenv()
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
    app.config["WTF_CSRF_ENABLED"] = os.getenv("WTF_CSRF_ENABLED")
    app.config["FLASK_ADMIN_SWATCH"] = os.getenv("FLASK_ADMIN_SWATCH")

    db.init_app(app)
    admin.init_app(app)

    register_blueprints(app)
    login_manager.init_app(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(authors)
    app.register_blueprint(auth)
