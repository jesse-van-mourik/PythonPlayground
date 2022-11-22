class Cell:

    def __init__(self, x, y):
        self.x = x
        self.y = y


class Board:

    def __init__(self, x=25, y=25):
        self.board = []
        for i in range(y):
            self.board.append([])
            for j in range(x):
                self.board[i].append(Cell(j, i))


def board_from_form(form):
    board = Board()
    for form_element in form:
        values = cellvalues_from_string(form[form_element])
        board.board[int(values[0])][int(values[1])].comment = values[2]
        # dev notes
        if values[2] != "empty":
            # print("x = " + values[0] + " | y= " + values[1] + " | " + values[2])
            pass
    return board


def cellvalues_from_string(string_to_parse):
    result = string_to_parse.split(",")
    return result[0], result[1], result[2]
