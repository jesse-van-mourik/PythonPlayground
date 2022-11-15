from flask import Blueprint, render_template, request, flash
from board import board_from_form

bp = Blueprint('dijkstra', __name__)


@bp.route('/dijkstra', methods=('POST',))
def start_dijkstra():
    board = board_from_form(request.form).board
    dists = {}
    prevs = {}  # keeps track of the shortest path
    q = []

    for y in range(0, len(board)):
        for cell in board[y]:
            if cell.comment == 'wall':
                continue
            if cell.comment == 'start':
                dists[cell] = 0
            else:
                dists[cell] = float('inf')

            prevs[cell] = None
            q.append(cell)

    while len(q) > 0:
        curr = find_cell_with_min_dist(dists, q)
        if curr == float('inf'):
            # no solution can be found
            break

        print(str(curr.comment) + "X: " + str(curr.x) + " Y: " + str(curr.y))
        q.remove(curr)

        neighbors = get_neighbors(curr, board)
        for n in neighbors:
            if n in q and n.comment != 'end':
                alt = dists[curr] + 1
                if alt < dists[n]:
                    dists[n] = alt
                    n.comment = 'visited'
                    prevs[n] = curr
            elif n.comment == 'end':
                prevs[n] = curr
                update_shortest_path(prevs, n)
                return render_template('board.html', board=board)

    # no solution was found
    flash('No solution was found.')
    return render_template('board.html', board=board)


def update_shortest_path(prevs, target):
    path = []
    while target is not None:
        if target.comment != 'end' and target.comment != 'start':
            target.comment = 'shortest'
        path.insert(0, target)
        target = prevs[target]


def find_cell_with_min_dist(dists, Q):
    min_dist = float('inf')
    key = float('inf')
    for item in dists.items():
        if item[1] < min_dist and item[0] in Q:
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
