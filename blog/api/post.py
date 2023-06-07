from flask_combo_jsonapi import ResourceDetail, ResourceList
from combojsonapi.event.resource import EventsResource

from blog.schemas import PostSchema
from blog.models.database import db
from blog.models import Post


class PostListEvent(EventsResource):

    def event_get_count(self):
        return {'count': Post.query.count()}


class PostList(ResourceList):
    events = PostListEvent
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
