from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cards.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_card(color,num,fill, shape,photo):
    card_object = Card(color=color,num=num,fill = fill,shape = shape, photo = photo)
    session.add(card_object)
    session.commit()

def get_card_by_id(id):
    card = session.query(Card).filter_by(
      id=id).first()
    return card


def check_set(card1, card2, card3):
	Set = False
	if((card1.fill != card2.fill and card2.fill !=card3.fill and card1.fill != card3.fill) or (card1.fill == card2.fill and card2.fill ==card3.fill)):	
		if((card1.num != card2.num and card2.num !=card3.num and card1.num != card3.num) or (card1.num == card2.num and card2.num ==card3.num)):	
			if((card1.shape != card2.shape and card2.shape !=card3.shape and card1.shape != card3.shape) or (card1.shape == card2.shape and card2.shape ==card3.shape)):	
				if((card1.color != card2.color and card2.color !=card3.color and card1.color != card3.color) or (card1.color == card2.color and card2.color ==card3.color)):	
					Set = True
	return Set
