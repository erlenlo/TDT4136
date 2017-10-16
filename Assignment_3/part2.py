from node import Node
from graphics import draw
from algorithmes import astar


boards = [
    './boards/board-2-1.txt',
    './boards/board-2-2.txt',
    './boards/board-2-3.txt',
    './boards/board-2-4.txt',
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
            if lines[i][j] == 'w':
                nodes.append(Node(j, i, 100, description='Water'))
            if lines[i][j] == 'm':
                nodes.append(Node(j, i, 50, description='Mountain'))
            if lines[i][j] == 'f':
                nodes.append(Node(j, i, 10, description='Forest'))
            if lines[i][j] == 'g':
                nodes.append(Node(j, i, 5, description='Grassland'))
            if lines[i][j] == 'r':
                nodes.append(Node(j, i, 1, description='Road'))
            elif lines[i][j] == 'A':
                start = Node(j, i, 1)
                nodes.append(start)
            elif lines[i][j] == 'B':
                target = Node(j, i, 1)
                nodes.append(target)

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

    draw(nodes, path, open_nodes, closed_nodes, lines, './img/part2/' + board[9:-4] + '.png')