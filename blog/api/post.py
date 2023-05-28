from flask_combo_jsonapi import ResourceDetail, ResourceList
from blog.schemas import PostSchema
from blog.models.database import db
from blog.models import Post


class PostList(ResourceList):
    schema = PostSchema
    data_layer = {
        "session": db.session,
        "model": Post,
    }


class PostDetail(ResourceDetail):
    schema = PostSchema
    data_layer = {
        "session": db.session,
        "model": Post,
    }
