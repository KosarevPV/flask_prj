from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

from blog.user.views import USERS

post = Blueprint('post', __name__, url_prefix='/posts', static_folder='../static')

POSTS = {
    1: {
        'text': 'Контроллер с опцией детекции облизывания губ управляет устройствами и движениями в играх с помощью касаний языком',
        'author': 1
    },
    2: {
        'text': 'Sony и Ford получают новые патенты, а Intel теряет лидерство: дайджест главных новостей',
        'author': 2
    },
    3: {
        'text': 'Маск создал компанию X.AI для разработки решений в сфере искусственного интеллекта',
        'author': 3
    },
    4: {
        'text': 'SpaceX получила разрешение на орбитальный запуск Starship',
        'author': 4
    },
}


@post.route('/')
def post_list():
    return render_template('post/list.html', posts=POSTS, users=USERS)


@post.route('/<int:pk>')
def get_post(pk: int):
    try:
        post_text = POSTS[pk]['text']
        post_author = USERS[POSTS[pk]['author']]
    except KeyError:
        raise NotFound(f'Post id {pk} not found')
    return render_template('post/details.html', post_text=post_text, post_author=post_author)
