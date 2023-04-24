from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {1: 'Curtis', 2: 'Gary', 3: 'Eustace', 4: 'John', 5: 'Harry'}


@user.route('/')
def user_list():
    return render_template('user/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    try:
        user_name = USERS[pk]
    except KeyError:
        raise NotFound(f'Users id {pk} not found')
    return render_template('user/details.html',user_name=user_name)
