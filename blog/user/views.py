from flask import Blueprint, render_template

user = Blueprint('user', __name__, url_prefix='/users', static_folder='../static')

USERS = {1: 'Curtis', 2: 'Gary', 3: 'Eustace', 4: 'John', 5: 'Harry'}


@user.route('/')
def user_list():
    return render_template('user/list.html', users=USERS)


@user.route('/<int:pk>')
def get_user(pk: int):
    return f'Hello user {pk}'
