from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = '2e6aba4de73f0f159a34cf30fb47e58d'
# relative path is specfied using /// 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sites.db'
# create a db instance
db = SQLAlchemy(app)

# Initialize the Flask application
app.app_context().push()

# Now you're within the application context, and you can safely perform database operations
db.create_all()

bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# 'login' - function name
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes