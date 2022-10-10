from flask import Blueprint, render_template, request
from board import Board, board_from_form

bp = Blueprint('movement', __name__)


@bp.route('/right/<original_x>/<original_y>', methods=('POST',))
def step_right(original_x, original_y):
    print("Original x: " + original_x + " original y: " + original_y)

    board = board_from_form(request.form)
    board.board[int(original_y)][int(original_x)+1].comment = 'visited'

    return render_template('board.html', board=board.board)
