from model import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cards.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_card(color,num,fill,shape,photo):
    card_object = Card(color=color,num=num,fill = fill,shape = shape, photo = photo)
    session.add(card_object)
    session.commit()

def create_counter(num_of_sets):
    num = Count(num_of_sets = num_of_sets)
    session.add(num)
    session.commit()

def add_set(id):
    add = session.query(Count).filter_by(id=id).first()
    (add.num_of_sets)+=1;
    session.commit()

def create_board_card(color,num,fill,shape,photo):
    card_object = Board(color=color,num=num,fill = fill,shape = shape, photo = photo)
    session.add(card_object)
    session.commit()

def get_card_by_id(id):
    card1 = session.query(Card).filter_by(id=id).first()
    return card1

def get_count_by_id(id):
    c1 = session.query(Count).filter_by(id=id).first()
    return c1


def get_board_card_by_id(id):
    card1 = session.query(Board).filter_by(id=id).first()
    return card1

def get_all_cards():
    cards = session.query(Card).all()
    return cards

def delete_board():
  session.query(Board).delete()
  session.commit()

def check_set(card1, card2, card3):
	Set = "not a set :("
	if((card1.fill != card2.fill and card2.fill !=card3.fill and card1.fill != card3.fill) or (card1.fill == card2.fill and card2.fill ==card3.fill)):	
		Set = "not a set :("
		if((card1.num != card2.num and card2.num !=card3.num and card1.num != card3.num) or (card1.num == card2.num and card2.num ==card3.num)):	
			Set = "not a set :("		
			if((card1.shape != card2.shape and card2.shape !=card3.shape and card1.shape != card3.shape) or (card1.shape == card2.shape and card2.shape == card3.shape )):	
				Set = "not a set :("
				if((card1.color != card2.color and card2.color !=card3.color and card1.color != card3.color) or (card1.color == card2.color and card2.color ==card3.color)):	
					Set = "a SET!!!"
	return Set