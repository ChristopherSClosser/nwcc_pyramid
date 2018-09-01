"""NWCC info model."""

from sqlalchemy import (
    Column,
    Integer,
    Text,
    Date
)

from .meta import Base


class MyModel(Base):
    """."""

    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    page = Column(Text)
    category = Column(Text)
    subcategory = Column(Text)
    title = Column(Text)
    img = Column(Text)
    imgsrc = Column(Text)
    markdown = Column(Text)
    extra = Column(Text)
    date = Column(Date)


# Index('my_index', MyModel.name, unique=True, mysql_length=255)
