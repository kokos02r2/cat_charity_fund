from app.core.db import CommonBase
from sqlalchemy import Column, String, Text


class CharityProject(CommonBase):
    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
