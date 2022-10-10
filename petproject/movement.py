from flask import Blueprint, render_template, request
from board import Board, board_from_form

bp = Blueprint('movement', __name__)


@bp.route('/right', methods=('POST',))
def step_right():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board.board[cell.y][cell.x + 1].comment = "visited"
                print()

    return render_template('board.html', board=board.board)
