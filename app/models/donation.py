from app.core.db import CommonBase
from sqlalchemy import Column, ForeignKey, Integer, Text


class Donation(CommonBase):
    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text, nullable=True)
