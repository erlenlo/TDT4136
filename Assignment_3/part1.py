from node import Node
from graphics import draw
from algorithmes import astar


boards = [
    './boards/board-1-1.txt',
    './boards/board-1-2.txt',
    './boards/board-1-3.txt',
    './boards/board-1-4.txt',
]

for board in boards:
    nodes = []
    open_nodes = []
    closed_nodes = []

    start = None
    target = None

    file = open(board, 'r')

    """
    Initialize nodes by reading the board
    """
    lines = [line.strip('\n') for line in file]
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '.':
                nodes.append(Node(j, i, 1))
            elif lines[i][j] == 'A':
                start = Node(j, i, 1)
                nodes.append(start)
            elif lines[i][j] == 'B':
                target = Node(j, i, 1)
                nodes.append(target)
            elif lines[i][j] == '#':
                nodes.append(Node(j, i, 1, True))

    target.target = True
    start.start = True
    
    path = []
    
    if astar(start, target, nodes, open_nodes, closed_nodes):
        node = target
        while node != start:
            path.append(node)
            node = node.parent
        path.append(start)
    else:
        print("No path from start to target found :(((")

    draw(nodes, path, open_nodes, closed_nodes, lines, './img/part1/' + board[9:-4] + '.png')