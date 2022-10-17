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


@bp.route('/step_left', methods=('POST',))
def call_step_left():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board = step_left(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


@bp.route('/step_right', methods=('POST',))
def call_step_right():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board = step_right(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


@bp.route('/step_up', methods=('POST',))
def call_step_up():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board = step_up(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


@bp.route('/step_down', methods=('POST',))
def call_step_down():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board = step_down(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


@bp.route('/step_up_left', methods=('POST',))
def call_step_up_left():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board = step_up_left(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


@bp.route('/step_up_right', methods=('POST',))
def call_step_up_right():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board = step_up_right(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


@bp.route('/step_down_left', methods=('POST',))
def call_step_down_left():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board = step_down_left(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


@bp.route('/step_down_right', methods=('POST',))
def call_step_down_right():
    board = board_from_form(request.form)
    for col in board.board:
        for cell in col:
            if cell.comment == "start":
                board = step_down_right(cell.x, cell.y, board)

    return render_template('board.html', board=board.board)


def step_right(original_x, original_y, board):
    # until end of board is reached or the given finish tile is reached
    if check_right_bound(original_x, original_y, board):
        return board

    # visit next tile
    board.board[original_y][original_x + 1].comment = "visited"
    return board


def step_left(original_x, original_y, board):
    # until end of board is reached or the given finish tile is reached
    if check_left_bound(original_x, original_y, board):
        return board

    # visit next tile
    board.board[original_y][original_x - 1].comment = "visited"
    return board


def step_up(original_x, original_y, board):
    # until end of board is reached or the given finish tile is reached
    if check_upper_bound(original_x, original_y, board):
        return board

    # visit next tile
    board.board[original_y-1][original_x].comment = "visited"
    return board


def step_down(original_x, original_y, board):
    # until end of board is reached or the given finish tile is reached
    if check_lower_bound(original_x, original_y, board):
        return board

    # visit next tile
    board.board[original_y+1][original_x].comment = "visited"
    return board


def step_up_left(original_x, original_y, board):
    # until end of board is reached or the given finish tile is reached
    if check_upper_left_bound(original_x, original_y, board):
        return board

    # visit next tile
    board.board[original_y-1][original_x-1].comment = "visited"
    return board


def step_up_right(original_x, original_y, board):
    # until end of board is reached or the given finish tile is reached
    if check_upper_right_bound(original_x, original_y, board):
        return board

    # visit next tile
    board.board[original_y-1][original_x+1].comment = "visited"
    return board


def step_down_right(original_x, original_y, board):
    # until end of board is reached or the given finish tile is reached
    if check_lower_right_bound(original_x, original_y, board):
        return board

    # visit next tile
    board.board[original_y+1][original_x+1].comment = "visited"
    return board


def step_down_left(original_x, original_y, board):
    # until end of board is reached or the given finish tile is reached
    if check_lower_left_bound(original_x, original_y, board):
        return board

    # visit next tile
    board.board[original_y+1][original_x-1].comment = "visited"
    return board


# returns true if boundary is encountered
def check_right_bound(original_x, original_y, board):
    return original_x == len(board.board[1]) - 1 or board.board[original_y][original_x + 1].comment == "end"


def check_left_bound(original_x, original_y, board):
    return original_x == 0 or board.board[original_y][original_x - 1].comment == "end"


def check_upper_bound(original_x, original_y, board):
    return original_y == 0 or board.board[original_y-1][original_x].comment == "end"


def check_lower_bound(original_x, original_y, board):
    return original_y == len(board.board) - 1 or board.board[original_y + 1][original_x].comment == "end"


def check_upper_left_bound(original_x, original_y, board):
    return original_y == 0 or \
            original_x == 0 or \
            board.board[original_y - 1][original_x - 1].comment == "end"


def check_upper_right_bound(original_x, original_y, board):
    return original_y == 0 or \
            original_x == len(board.board[1]) - 1 or \
            board.board[original_y - 1][original_x + 1].comment == "end"


def check_lower_right_bound(original_x, original_y, board):
    return original_y == len(board.board) - 1 or \
            original_x == len(board.board[1]) - 1 or \
            board.board[original_y + 1][original_x + 1].comment == "end"


def check_lower_left_bound(original_x, original_y, board):
    return original_y == len(board.board) - 1 or \
            original_x == 0 or \
            board.board[original_y + 1][original_x - 1].comment == "end"
