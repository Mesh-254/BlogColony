from flask import Blueprint
from flask import render_template, request, Blueprint
from app.models import Post, User
from flask_login import login_required

# create an instance of the blueprint
main = Blueprint('main', __name__)


@main.route('/')
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    post = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=10)
    return render_template('main/index.html', post=post)

@main.route('/blogs')
def all_posts():
    # Get all posts and paginate them
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    post = Post.query.all()
    return render_template("home.html", posts=post)



@main.route('/about/')
def about():
    return render_template('about.html', title='About')