from flask import Blueprint, render_template, request
from board import board_from_form

bp = Blueprint('dijkstra', __name__)


@bp.route('/dijkstra', methods=('POST',))
def start_dijkstra():
    board = board_from_form(request.form).board
    dists = {}
    prevs = {}
    Q = []

    for y in range(0, len(board)):
        for cell in board[y]:
            if cell.comment == 'wall':
                continue
            if cell.comment == 'start':
                print('start found')
                dists[cell] = 0
            else:
                dists[cell] = float('inf')

            prevs[cell] = None

            if cell.comment == 'end':
                print('end found #1')
            Q.append(cell)

    while len(Q) > 0:
        curr = find_cell_with_min_dist(dists, Q)
        # if curr.comment == 'end':
        #    print('end found #2')
        #    break
        print(str(curr.comment) + "X: " + str(curr.x) + " Y: " + str(curr.y))
        Q.remove(curr)

        neighbors = get_neighbors(curr, board)
        for n in neighbors:
            if n in Q and n.comment != 'end':
                alt = dists[curr] + 1
                if alt < dists[n]:
                    dists[n] = alt
                    n.comment = 'visited'
                    prevs[n] = curr
            elif n.comment == 'end':
                print('end found #3')
                prevs[n] = curr
                update_shortest_path(prevs, n)
                return render_template('board.html', board=board)

    return render_template('board.html', board=board)


def update_shortest_path(prevs, target):
    path = []
    while target is not None:
        print('SHORTEST')
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

    # northern
    neighbors.append(board[max(cell.y - 1, 0)][cell.x])
    # southern
    neighbors.append(board[min(cell.y + 1, len(board[0])-1)][cell.x])
    # western
    neighbors.append(board[cell.y][max(cell.x - 1, 0)])
    # eastern
    neighbors.append(board[cell.y][min(cell.x + 1, len(board[0])-1)])

    return neighbors
