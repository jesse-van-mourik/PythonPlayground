from flask import Blueprint, render_template, request, make_response, url_for, redirect
from board import Cell, Board


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return render_template('home.html')


@bp.route('/cellform')
def display_cell_form():
    return render_template('cellform.html')


@bp.route('/createcell', methods=('POST',))
def create_cell():
    board = Board(25, 25)
    x = int(request.form['cellx']) - 1
    y = int(request.form['celly']) - 1
    board.board[x][y].comment = 'X'
    return render_template('board.html', board=board.board)



