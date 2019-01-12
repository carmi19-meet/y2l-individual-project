from flask import Flask, request
from flask import render_template
from database import create_card, get_card_by_id, check_set
app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR-VERY-SECRET-SHHH'

@app.route('/')
def home():
	return render_template("home.html")
	

@app.route('/set/board', methods=['GET', 'POST'])
def set_board():
    sets = []
    for i in range 12:
        set[i] = get_card_by_id(random.randint(1,82))
    if request.method == 'GET':
        return render_template("board.html", Set = 	False, first_run = True,sets = sets)
    else:
        card1 = request.form['line1']
        card2 = request.form['line2']
        card3 = request.form['line3']
        Set = check_set(card1,card2,card3)
        return render_template('home.html',Set = Set, first_run = False, sets = sets)


@app.route('/dont_go_here')
def cards_creator():
	create_card("green",1,"line", "snake","link!!!")
	create_card("purple",2,"full", "diamond","link!!!")
	create_card("red",3,"empty", "ellipse","link!!!")
	return render_template("dont.html")

if __name__ == '__main__':
    app.run(debug=True)	