from flask import Flask, request
from flask import render_template
from database import create_card, get_card_by_id, check_set, get_all_cards, create_board_card, get_board_card_by_id, delete_board, create_counter, add_set, get_count_by_id, delete_counter
import random
import time
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def home():
	return render_template("home.html")

@app.route('/rules')
def learn_to_play():
	return render_template("rules.html")
	
@app.route('/about')
def about_set():
	return render_template("about.html")	

@app.route('/set/board/1', methods=['GET', 'POST'])
def set_board():

    if request.method == 'GET':
    	delete_board()
    	delete_counter()
    	create_counter(0)
    	counter = get_count_by_id(1)
    	delete_board()
    	x = random.randint(1, 82)
        a = get_card_by_id(x)
        sets = []
        for i in range (13):
            already = True
            x = random.randint(1, 82)
            while already==True:
                already = False
                x = random.randint(1, 82)
                a = get_card_by_id(x)
                for y in range (len(sets)):
                    if (a == sets[y]):
                        already = True
            sets.append(get_card_by_id(x))
            create_board_card(a.color,a.num,a.fill,a.shape,a.photo)
        return render_template("board.html", Set = "No set", first_run = True,sets = sets, counter = counter)
    else:
    	sets = []
    	Set = "not a set, pick only three cards..."
    	counter = get_count_by_id(1)
    	for i in range (13):
    		sets.append(get_board_card_by_id(i+1))
    	if (len(request.form.getlist("cards")) >=3):
        	card1 = sets[int(request.form.getlist("cards") [0])]
        	card2 = sets[int(request.form.getlist("cards") [1])]
        	card3 = sets[int(request.form.getlist("cards") [2])]
        	Set = check_set(card1,card2,card3)
        
        if Set == "a SET!!!":
        	add_set(1)
       	return render_template('board.html',Set = Set, first_run = False, sets = sets,counter = counter)


@app.route('/set/board/2', methods=['GET', 'POST'])
def set_board2():

    if request.method == 'GET':
    	delete_board()
        sets = []
        for i in range (13):
            already = True
            x = random.randint(1, 82)
            while already==True:
                already = False
                x = random.randint(1, 82)
                a = get_card_by_id(x)
                for y in range (len(sets)):
                    if (a == sets[y]):
                        already = True
            sets.append(get_card_by_id(x))
            create_board_card(a.color,a.num,a.fill,a.shape,a.photo)
        return render_template("board2.html", Set = "No set", first_run = True,sets = sets)
    else:
    	Set = "not a set, pick only three cards..."
    	sets = []
    	for i in range (13):
    		sets.append(get_board_card_by_id(i+1))
    	if (len(request.form.getlist("cards")) >=3):
        	card1 = sets[int(request.form.getlist("cards") [0])]
        	card2 = sets[int(request.form.getlist("cards") [1])]
        	card3 = sets[int(request.form.getlist("cards") [2])]
        	Set = check_set(card1,card2,card3)

        sets = []
        x = random.randint(1, 82)
        a = get_card_by_id(x)
    	for i in range (13):
            already = True
            x = random.randint(1, 82)
            a = get_card_by_id(x)
            while already==True:
                already = False
                x = random.randint(1, 82)           
                a = get_card_by_id(x)
                for y in range (len(sets)):
                    if (a == sets[y]):
                        already = True
            sets.append(get_card_by_id(x))
            create_board_card(a.color,a.num,a.fill,a.shape,a.photo)
       	return render_template('board2.html',Set = Set, first_run = False, sets = sets)

@app.route('/dont_go_here')
def cards_creator():
	create_card("red","1","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/1.png")
	create_card("red","2","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/2.png")
	create_card("red","3","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/3.png")
	create_card("purple","1","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/4.png")
	create_card("purple","2","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/5.png")
	create_card("purple","3","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/6.png")
	create_card("green","1","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/7.png")
	create_card("green","2","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/8.png")
	create_card("green","3","full","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/9.png")
	create_card("red","1","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/10.png")
	create_card("red","2","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/11.png")
	create_card("red","3","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/12.png")
	create_card("purple","1","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/13.png")
	create_card("purple","2","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/14.png")
	create_card("purple","3","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/15.png")
	create_card("green","1","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/16.png")
	create_card("green","2","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/17.png")
	create_card("green","3","full","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/18.png")
	create_card("red","1","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/19.png")
	create_card("red","2","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/20.png")
	create_card("red","3","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/21.png")
	create_card("purple","1","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/22.png")
	create_card("purple","2","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/23.png")
	create_card("purple","3","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/24.png")
	create_card("green","1","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/25.png")
	create_card("green","2","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/26.png")
	create_card("green","3","full","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/27.png")
	create_card("red","1","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/28.png")
	create_card("red","2","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/29.png")
	create_card("red","3","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/30.png")
	create_card("purple","1","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/31.png")
	create_card("purple","2","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/32.png")
	create_card("purple","3","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/33.png")
	create_card("green","1","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/34.png")
	create_card("green","2","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/35.png")
	create_card("green","3","line","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/36.png")
	create_card("red","1","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/37.png")
	create_card("red","2","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/38.png")
	create_card("red","3","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/39.png")
	create_card("purple","1","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/40.png")
	create_card("purple","2","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/41.png")
	create_card("purple","3","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/42.png")
	create_card("green","1","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/43.png")
	create_card("green","2","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/44.png")
	create_card("green","3","line","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/45.png")
	create_card("red","1","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/46.png")
	create_card("red","2","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/47.png")
	create_card("red","3","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/48.png")
	create_card("purple","1","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/49.png")
	create_card("purple","2","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/50.png")
	create_card("purple","3","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/51.png")
	create_card("green","1","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/52.png")
	create_card("green","2","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/53.png")
	create_card("green","3","line","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/54.png")
	create_card("red","1","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/55.png")
	create_card("red","2","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/56.png")
	create_card("red","3","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/57.png")
	create_card("purple","1","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/58.png")
	create_card("purple","2","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/59.png")
	create_card("purple","3","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/60.png")
	create_card("green","1","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/61.png")
	create_card("green","2","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/62.png")
	create_card("green","3","empty","snake","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/63.png")
	create_card("red","1","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/64.png")
	create_card("red","2","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/65.png")
	create_card("red","3","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/66.png")
	create_card("purple","1","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/67.png")
	create_card("purple","2","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/68.png")
	create_card("purple","3","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/69.png")
	create_card("green","1","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/70.png")
	create_card("green","2","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/71.png")
	create_card("green","3","empty","diamond","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/72.png")
	create_card("red","1","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/73.png")
	create_card("red","2","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/74.png")
	create_card("red","3","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/75.png")
	create_card("purple","1","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/76.png")
	create_card("purple","2","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/77.png")
	create_card("purple","3","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/78.png")
	create_card("green","1","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/79.png")
	create_card("green","2","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/80.png")
	create_card("green","3","empty","ellipse","https://www.setgame.com/sites/all/modules/setgame_set/assets/images/new/81.png")
	return render_template("home.html")

if __name__ == '__main__':
    app.run(debug=True)	