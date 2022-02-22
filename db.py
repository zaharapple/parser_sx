from sqlalchemy import Column, ForeignKey, Integer, String, Text, Date, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Item(Base):

    __tablename__ = 'item'
    __tableargs__ = {
        'comment': 'аа'
    }

    id = Column(
        Integer,
        nullable=False,
        unique=True,
        primary_key=True,
        autoincrement=True
    )
    name = Column(String(128), comment='Наименование товара')
    description = Column(Text, comment='Описание')
    price =