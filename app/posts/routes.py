from flask import Blueprint, render_template, url_for, flash, redirect, request, abort, current_app
from flask_login import current_user, login_required
from app import db
from app.models import Post
from app.posts.forms import PostForm
from werkzeug.utils import secure_filename

import os
import secrets
# create an instance of the blueprint
posts = Blueprint('posts', __name__)


def save_image(image):
    hash_photo = secrets.token_urlsafe(10)
    _, file_extension = os.path.splitext(image.filename)
    image_name = hash_photo + file_extension
    file_path = os.path.join(current_app, root_path, 'static/images', image)
    image.save(file_path)
    return image_name


@login_required
@posts.route('/post/new', methods=['GET', 'POST'])
def new_post():
    image_path = None
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        image_data = form.image.data
        image_filename = secure_filename(image_data.filename)
        
        # Save the image to the static folder
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
        image_data.save(image_path)

        post = Post(title=form.title.data,
                    image=image_filename,
                    content=form.content.data,
                    author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your Post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form,
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
