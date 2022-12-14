from flask import Blueprint, render_template, request, flash
from board import board_from_form

application = Blueprint('dijkstra', __name__)


@application.route('/dijkstra', methods=('POST',))
def start_dijkstra():
    board, solution_found = perform_dijkstra(board_from_form(request.form).board)

    if solution_found:
        counts = calculate_num_visited(board)
        flash('A solution was found!')
        flash('Tiles visited: ' + str(counts[0]))
        flash('Path length: ' + str(counts[1]))
        return render_template('board.html', board=board)

    # no solution was found
    flash('No solution was found.')
    return render_template('board.html', board=board)


def perform_dijkstra(board):
    dists = {}
    prevs = {}  # keeps track of the shortest path
    q = []  # the list of cells to visit

    # initialize lists with default values
    for y in range(0, len(board)):
        for cell in board[y]:
            if cell.comment == 'wall':
                continue
            if cell.comment == 'start':
                dists[cell] = 0
            else:
                dists[cell] = float('inf')  # infinite distance means not-yet-visited

            prevs[cell] = None
            q.append(cell)

    while len(q) > 0:
        curr = find_cell_with_min_dist(dists, q)
        if curr == float('inf'):
            # no solution can be found
            break

        # print(str(curr.comment) + "X: " + str(curr.x) + " Y: " + str(curr.y))
        q.remove(curr)

        # note: neighbors in four directions, no diagonals.
        neighbors = get_neighbors(curr, board)
        for n in neighbors:
            if n in q and n.comment != 'end':
                alt = dists[curr] + 1
                if alt < dists[n]:  # is the neighbor not visited yet, or did we find a shorter route to it?
                    dists[n] = alt
                    n.comment = 'visited'
                    prevs[n] = curr
            elif n.comment == 'end':
                prevs[n] = curr
                update_shortest_path(prevs, n)
                return board, True

    return board, False


def update_shortest_path(prevs, target):
    path = []
    while target is not None:
        if target.comment != 'end' and target.comment != 'start':
            target.comment = 'shortest'
        path.insert(0, target)
        target = prevs[target]


def find_cell_with_min_dist(dists, q):
    # where q is the set of cells to visit
    min_dist = float('inf')
    key = float('inf')
    for item in dists.items():
        if item[1] < min_dist and item[0] in q:
            min_dist = item[1]
            key = item[0]

    return key


def get_neighbors(cell, board):
    neighbors = []
    # longer code for readability
    # northern
    neighbors.append(board[max(cell.y - 1, 0)][cell.x])
    # southern
    neighbors.append(board[min(cell.y + 1, len(board[0])-1)][cell.x])
    # western
    neighbors.append(board[cell.y][max(cell.x - 1, 0)])
    # eastern
    neighbors.append(board[cell.y][min(cell.x + 1, len(board[0])-1)])

    return neighbors


def calculate_num_visited(board):
    count_visited = 0
    count_shortest = 0
    for y in range(0, len(board[0])):
        for cell in board[y]:
            if cell.comment == 'visited':
                count_visited += 1
            if cell.comment == 'shortest':
                count_shortest += 1
                count_visited += 1

    return [count_visited, count_shortest]


@application.route('/boardreset', methods=('POST',))
def board_reset():
    print('resetting board')
    board = board_from_form(request.form).board

    for y in range(0, len(board[0])):
        for cell in board[y]:
            if cell.comment != 'wall' and cell.comment != 'start' and cell.comment != 'end':
                cell.comment = None

    return render_template('board.html', board=board)



