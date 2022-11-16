from flask import Blueprint, render_template, request, make_response, url_for, redirect
from board import Board


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('home.html')


@bp.route('/cellform')
def display_cell_form():
    return render_template('cellform.html')


@bp.route('/board', methods=('POST',))
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


@bp.route('/message', methods=("POST",))
def print_message():
    for cell in request.form:
        print(cell)

    print('button is pressed')



