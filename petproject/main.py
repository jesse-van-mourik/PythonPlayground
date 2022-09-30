from flask import Blueprint, render_template, request, make_response, url_for, redirect
from board import Cell, Board


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('home.html')


@bp.route('/cellform')
def display_cell_form():
    return render_template('cellform.html')


@bp.route('/board', methods=('POST',))
def create_cell():
    board = Board(25, 25)
    wall1x = int(request.form['wall1x']) - 1
    wall1y = int(request.form['wall1y']) - 1
    board.board[wall1x][wall1y].comment = 'wall'

    startx = int(request.form['startx']) - 1
    starty = int(request.form['starty']) - 1
    board.board[startx][starty].comment = 'start'
    return render_template('board.html', board=board.board)


@bp.route('/message')
def print_message():
    print('button is pressed')



