from flask_combo_jsonapi import ResourceDetail, ResourceList

from blog.permissions.user import UserPermissionGet, UserPermissionPatch
from blog.schemas import UserSchema
from blog.models.database import db
from blog.models import User


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_get": [UserPermissionGet],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        "session": db.session,
        "model": User,
        "permission_patch": [UserPermissionPatch],
    }
