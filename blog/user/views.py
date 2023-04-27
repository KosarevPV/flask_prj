from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.models import User

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')


@user.route('/', endpoint="list")
def user_list():
    users = User.query.all()
    return render_template('user/list.html', users=users)


@user.route('/<int:user_id>', endpoint="details")
def user_details(user_id: int):
    user = User.query.filter_by(id=user_id).one_or_none()
    if user is None:
        raise NotFound(f'Users id {user_id} not found')

    return render_template('user/details.html',user=user)
