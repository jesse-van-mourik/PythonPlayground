from flask import Blueprint, render_template, request
from board import board_from_form
import time
bp = Blueprint('movement', __name__)


@bp.route('/right', methods=('POST',))
def right_until_stopped():
    board = board_from_form(request.form)

    for col in board.board:
        for cell in col:
            if cell.comment == "end":
                return render_template('board.html', board=board.board)
            if cell.comment == "start" or cell.comment == "visited":
                board = step_right(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


def step_right(original_x, original_y, board):
    if board.board[original_y][original_x + 1].comment == "end":
        return board
    board.board[original_y][original_x + 1].comment = "visited"
    return board
