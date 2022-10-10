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
def create_cell():
    board = Board()
    wall1x = int(request.form['wall1x']) - 1
    wall1y = int(request.form['wall1y']) - 1
    board.board[wall1y][wall1x].comment = 'wall'

    startx = int(request.form['startx']) - 1
    starty = int(request.form['starty']) - 1
    board.board[starty][startx].comment = 'start'
    return render_template('board.html', board=board.board)


@bp.route('/message', methods=("POST",))
def print_message():
    for cell in request.form:
        print(cell)

    print('button is pressed')



