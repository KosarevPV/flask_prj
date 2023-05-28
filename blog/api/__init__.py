from flask_combo_jsonapi import Api
from combojsonapi.spec import ApiSpecPlugin

from blog.api.tag import TagList, TagDetail
from blog.api.user import UserList, UserDetail
from blog.api.author import AuthorList, AuthorDetail
from blog.api.post import PostList, PostDetail


def create_api_spec_pluugin(app):
    api_spec_plugin = ApiSpecPlugin(
        app=app,
        tags={
            "Tag": "Tag API",
            "User": "User API",
            "Author": "Author API",
            "Post": "Post API",

        }
    )
    return api_spec_plugin


def init_api(app):
    api_spec_plugin = create_api_spec_pluugin(app)
    api = Api(
        app,
        plugins=[
            api_spec_plugin
        ]
    )

    api.route(TagList, "tag_list", "/api/tags", tag="Tag")
    api.route(TagDetail, "tag_detail", "/api/tags/<int:id>/", tag="Tag")
    api.route(UserList, "user_list", "/api/users", tag="User")
    api.route(UserDetail, "user_detail", "/api/users/<int:id>/", tag="User")
    api.route(AuthorList, "author_list", "/api/authors", tag="Author")
    api.route(AuthorDetail, "author_detail", "/api/authors/<int:id>/", tag="Author")
    api.route(PostList, "post_list", "/api/posts", tag="Post")
    api.route(PostDetail, "post_detail", "/api/posts/<int:id>/", tag="Post")

    return api
