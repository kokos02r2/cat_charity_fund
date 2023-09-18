from sqlalchemy import Column, Integer, Text, ForeignKey
from app.core.db import CommonBase


class Donation(CommonBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
