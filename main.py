from flask import Blueprint, render_template, request
from board import Board

application = Blueprint('main', __name__)


@application.route('/')
def index():
    return render_template('home.html')


@application.route('/cellform')
def display_cell_form():
    return render_template('cellform.html')


@application.route('/board', methods=('POST',))
def create_board():
    board = Board()
    for i in range(1, 11):
        key_x = 'wall' + str(i) + 'x'
        key_y = 'wall' + str(i) + 'y'
        wall_x = int(request.form[key_x]) - 1
        wall_y = int(request.form[key_y]) - 1
        board.board[wall_y][wall_x].comment = 'wall'

    startx = int(request.form['startx']) - 1
    starty = int(request.form['starty']) - 1
    board.board[starty][startx].comment = 'start'

    endx = int(request.form['endx']) - 1
    endy = int(request.form['endy']) - 1
    board.board[endy][endx].comment = 'end'

    return render_template('board.html', board=board.board)

@application.route('/stats', methods=('GET',))
def open_stats_page():
    return render_template('stats.html')





