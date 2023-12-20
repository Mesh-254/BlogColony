from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from app.config import Config
from flask_migrate import Migrate

# Create a db instance
db = SQLAlchemy()

bcrypt = Bcrypt()
login_manager = LoginManager()
# 'login' - function name
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def create_app(config_class=Config):
    app = Flask(__name__)
    
    app.config['UPLOAD_FOLDER'] = 'static/images'

    # Set strict_slashes to False
    app.url_map.strict_slashes = False

    app.config.from_object(config_class)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    migrate = Migrate(app, db)


    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    @app.route('/')
    @app.route('/home')
    def index():
        return render_template('main/index.html')

    return app
