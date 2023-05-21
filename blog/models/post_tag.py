from sqlalchemy import Table, Column, Integer, ForeignKey
from blog.models.database import db


post_tag_association_table = Table(
    "post_tag_association",
    db.metadata,
    Column("post_id", Integer, ForeignKey("post.id"), nullable=False),
    Column("tag_id", Integer, ForeignKey("tag.id"), nullable=False),
)
