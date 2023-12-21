from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, current_app
from flask_login import current_user, login_required

import app
from app import db
from app.models import Post
from app.posts.forms import PostForm
from werkzeug.utils import secure_filename

import os
import secrets

# create an instance of the blueprint
posts = Blueprint('posts', __name__)


# def save_picture(post_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(post_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(current_app.root_path, 'static/pictures', picture_fn)
#     post_picture.save(picture_path)
#     return picture_fn


@login_required
@posts.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        # image = form.image.data
        # image_post = save_picture(image)
        post = Post(title=form.title.data,
                    content=form.content.data,
                    author=current_user)

        print(post)
        db.session.add(post)
        db.session.commit()
        flash('Your Post has been created!', 'success')
        return redirect(url_for('main.home'))

    # image = url_for('static', filename='images/' + form.image.data)
    return render_template('create_post.html', title='New Post', form=form, post=post,
                           legend='New Post')


@login_required
@posts.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)


@login_required
@posts.route('/post/<int:post_id>/update', methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title='Update Post', form=form, legend='Update Post')


@login_required
@posts.route('/post/<int:post_id>/delete', methods=['GET', 'POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.home', post_id=post.id))
