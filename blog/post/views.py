from flask import Blueprint, render_template, request, current_app, redirect, url_for
from flask_login import login_required, current_user
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound

from blog.models.database import db
from blog.models import Post, Author, Tag
from blog.forms.post import CreatePostForm

post = Blueprint('post', __name__, url_prefix='/posts', static_folder='../static')


@post.route('/', endpoint="list")
def post_list():
    posts = Post.query.all()
    return render_template('post/list.html', posts=posts)


@post.route('/<int:post_id>/', endpoint="details")
def post_details(post_id: int):
    post = Post.query.filter_by(id=post_id).options(joinedload(Post.tags)).one_or_none()
    if post is None:
        raise NotFound
    return render_template('post/details.html', post=post)

@post.route('/create/', methods=["GET", "POST"], endpoint="create")
@login_required
def create_post():
    error = None
    form = CreatePostForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by("name")]
    if request.method == "POST" and form.validate_on_submit():
        post = Post(title=form.title.data.strip(), body=form.body.data)

        if current_user.author:
            post.author_id = current_user.author.id
        else:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
            post.author_id = author.id

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                post.tags.append(tag)
        db.session.add(post)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new article!")
            error = "Could not create article!"
        else:
            return redirect(url_for("post.details", post_id=post.id))

    return render_template("post/create.html", form=form, error=error)


@post.route('/tags', endpoint="tag_list")
def tag_list():
    tags = Tag.query.all()
    return render_template('post/tag_list.html', tags=tags)


@post.route('tags/<int:tag_id>/', endpoint="tags_details")
def tag_details(tag_id: int):
    tag = Tag.query.filter_by(id=tag_id).options(joinedload(Tag.post)).one_or_none()
    if tag is None:
        raise NotFound

    return render_template('post/tag_details.html', tag=tag)
