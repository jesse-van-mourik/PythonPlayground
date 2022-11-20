from board import Board
from dijkstra import perform_dijkstra


class TestDijkstra:

    def test_perform_dijkstra_successful(self):
        board = Board().board
        set_start_and_finish(board)
        assert (perform_dijkstra(board)[1]) is True

    def test_perform_dijkstra_enclosed_start(self):
        board = Board().board
        set_start_and_finish(board)
        set_walls_around_start(board)
        assert (perform_dijkstra(board)[1]) is False

    def test_perform_dijkstra_enclosed_end(self):
        board = Board().board
        set_start_and_finish(board)
        set_walls_around_end(board)
        assert (perform_dijkstra(board)[1]) is False


def set_start_and_finish(board):
    board[2][2].comment = 'start'
    board[6][6].comment = 'end'
    return


def set_walls_around_start(board):
    board[1][1].comment = 'wall'
    board[1][2].comment = 'wall'
    board[1][3].comment = 'wall'
    board[2][1].comment = 'wall'
    board[2][3].comment = 'wall'
    board[3][1].comment = 'wall'
    board[3][2].comment = 'wall'
    board[3][3].comment = 'wall'
    return


def set_walls_around_end(board):
    board[5][5].comment = 'wall'
    board[5][6].comment = 'wall'
    board[5][7].comment = 'wall'
    board[6][5].comment = 'wall'
    board[6][7].comment = 'wall'
    board[7][5].comment = 'wall'
    board[7][6].comment = 'wall'
    board[7][7].comment = 'wall'
    return
