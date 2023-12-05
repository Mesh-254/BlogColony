from flask import Blueprint
from flask import render_template, request, Blueprint
from app.models import Post
from flask_login import login_required

# create an instance of the blueprint
main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home/')
@login_required
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('main/index.html', posts=posts)

@main.route('/about/')
def about():
    return render_template('about.html', title='About')