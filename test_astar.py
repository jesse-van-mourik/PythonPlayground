from board import Board
from astar import perform_astar
from test_dijkstra import set_walls_around_start, set_walls_around_end, set_start_and_finish


class TestAstar:

    def test_perform_astar_successful(self):
        board = Board().board
        set_start_and_finish(board)
        assert (perform_astar(board)[1]) is True

    def test_perform_astar_enclosed_start(self):
        board = Board().board
        set_start_and_finish(board)
        set_walls_around_start(board)
        assert (perform_astar(board)[1]) is False

    def test_perform_astar_enclosed_end(self):
        board = Board().board
        set_start_and_finish(board)
        set_walls_around_end(board)
        assert (perform_astar(board)[1]) is False



