from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import Config



# create a db instance
db = SQLAlchemy()

# Initialize the Flask application
Config.app_context().push()

# Now you're within the application context, and you can safely perform database operations
db.create_all()

bcrypt = Bcrypt()
login_manager = LoginManager()
# 'login' - function name
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    app.app_context().push()
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app