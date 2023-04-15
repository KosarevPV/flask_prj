from flask import Blueprint

post = Blueprint('post', __name__, url_prefix='/posts', static_folder='../static')


@post.route('/')
def user_list():
    return 'Hello posts'


@post.route('/<int:pk>')
def get_post(pk: int):
    return f'Hello post {pk}'