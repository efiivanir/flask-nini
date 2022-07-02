from flask import Flask
from flask_bootstrap import Bootstrap

from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user

from functools import wraps
from flask import g, request, redirect, url_for,flash
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.username != app.config['ADMIN_USER_NAME']:
            flash(f"Your account {current_user.username} not allowed to enter to this menue.")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

from app import routes,models
