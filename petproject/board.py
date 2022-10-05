class Cell:
    x = 0
    y = 0
    comment = ''

    def __init__(self, x, y):
        self.x = x;
        self.y = y;


class Board:

    def __init__(self, x, y):
        self.board = []
        for i in range(x):
            self.board.append([])
            for j in range(y):
                #board[i].append(Cell(i, j))
                self.board[i].append(Cell(j, i))
