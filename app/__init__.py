# app/__init__.py
from flask import Flask
from flask_login import LoginManager
from .models import User

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key_here'

    # Configure LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'main.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return users.get(user_id)

    from .views import main
    app.register_blueprint(main)

    return app