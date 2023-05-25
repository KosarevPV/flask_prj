from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from blog.models.database import db
from blog.models.post_tag import post_tag_association_table


class Tag(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")

    post = relationship("Post", secondary=post_tag_association_table, back_populates="tags")

    def __str__(self):
        return self.name