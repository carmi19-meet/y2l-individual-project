from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Write your classes here :
class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    color = Column(String) # green, red or purple
    num = Column(Integer) # 1,2 or 3
    fill = Column(String) # line, full or empty
    shape = Column(String) # snake, diamond or a ellipse 
    photo = Column(String) # the photo of the card

class Board(Base):
    __tablename__ = "board_cards"
    id = Column(Integer, primary_key=True)
    color = Column(String) # green, red or purple
    num = Column(Integer) # 1,2 or 3
    fill = Column(String) # line, full or empty
    shape = Column(String) # snake, diamond or a ellipse 
    photo = Column(String) # the photo of the card

class Count(Base):
    __tablename__ = "counter"
    id = Column(Integer, primary_key=True)
    num_of_sets = Column(Integer)
