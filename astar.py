from flask import Blueprint, render_template, request, flash
from board import board_from_form
from dijkstra import get_neighbors, calculate_num_visited

application = Blueprint('astar', __name__)


@application.route('/astar', methods=('POST',))
def start_astar():
    board, solution_found = perform_astar(board_from_form(request.form).board)

    if solution_found:
        counts = calculate_num_visited(board)
        flash('A solution was found!')
        flash('Tiles visited: ' + str(counts[0]))
        flash('Path length: ' + str(counts[1]))
        return render_template('board.html', board=board)

    flash('No solution was found.')
    return render_template('board.html', board=board)


def perform_astar(board):
    print("START A*")
    # heuristic = abs(target.x - curr.x) + abs(target.y - curr.y) aka Manhattan Distance
    start_and_end = find_start_and_end_cell(board)
    start_cell = start_and_end[0]
    end_cell = start_and_end[1]

    open_set = [start_cell]
    came_from = {}

    g_scores = {}
    f_scores = {}
    # set initial mappings
    for y in range(0, len(board)):
        for cell in board[y]:
            g_scores[cell] = float('inf')
            f_scores[cell] = float('inf')

    g_scores[start_cell] = 0
    f_scores[start_cell] = heuristic_score(start_cell, end_cell)

    # start of actual algorithm
    while len(open_set) > 0:
        # f-score is a sum of the cost of getting to that tile plus the estimated cost
        # of getting to the final destination (as determined by the heuristic).
        # The cell with the lowest f-score will be investigated next.
        curr = find_next_current_cell(open_set, f_scores)
        open_set.remove(curr)

        # gets four direction neighbours, no diagonals
        neighbors = get_neighbors(curr, board)
        for n in neighbors:
            if n == end_cell:
                print('end was reached')
                came_from[n] = curr
                reconstruct_path(came_from, curr)
                return board, True
            if n.comment == 'wall':
                continue
            else:
                if n != start_cell and n != end_cell:
                    n.comment = 'visited'
                tentative_g_score = g_scores[curr] + 1
                if tentative_g_score < g_scores[n]:
                    came_from[n] = curr
                    g_scores[n] = tentative_g_score
                    f_scores[n] = tentative_g_score + heuristic_score(n, end_cell)
                    # print(str(n.x) + ", " + str(n.y) + " n of: " + str(curr.x) + ", " + str(curr.y) + " with f: " + str(
                    #    f_scores[n]))
                    if n not in open_set:
                        open_set.append(n)

    print('no solution')
    return board, False


def find_start_and_end_cell(board):
    result = [None, None]
    for y in range(0, len(board)):
        for cell in board[y]:
            if cell.comment == 'start':
                print('start tile found')
                result[0] = cell
            if cell.comment == 'end':
                print('end tile found')
                result[1] = cell
            if result[0] is not None and result[1] is not None:
                return result

    return result


def heuristic_score(cell, end_cell):
    # manhattan distance
    return abs(cell.x - end_cell.x) + abs(cell.y - end_cell.y)


def find_next_current_cell(open_set, f_scores):
    # find cell with lowest f-score
    min_value = float('inf')
    next_current = None
    for cell in open_set:
        if f_scores[cell] < min_value:
            min_value = f_scores[cell]
            next_current = cell
    return next_current


def reconstruct_path(came_from, current):
    # visualize the shortest path
    keys = list(came_from.keys())
    while current in keys:
        if current.comment != 'start':
            current.comment = 'shortest'
        current = came_from[current]



