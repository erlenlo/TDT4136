from node import Node
import bisect

def astar(start, target, nodes, open_nodes, closed_nodes):
    """
    Pathfinding algorithm to find shortest path from A to B
    :param start: Start node
    :param target: Target node
    :param nodes: All nodes
    :param open_nodes: Open nodes left unchecked during path resolve
    :param closed_nodes: Checked nodes during path resolve
    :return True if path is found, False if not
    """
    start.h_score = distance(start, target)
    start.f_score = start.h_score
    open_nodes.append(start)

    while open_nodes:
        current = open_nodes.pop(0)
        closed_nodes.append(current)
        initialize_children(current, nodes)

        if current.target:
            return True

        for child in current.children:
            estimate = distance(child, target)
            temp_g_score = current.g_score + child.cost
            temp_f_score = temp_g_score + estimate

            if child in closed_nodes and temp_f_score >= child.f_score:
                continue

            if child not in open_nodes or temp_f_score < child.f_score:
                child.parent = current
                child.f_score = temp_f_score
                child.g_score = temp_g_score
                child.h_score = estimate
                if child in open_nodes:
                    open_nodes.remove(child)
                
                bisect.insort(open_nodes, child) # Insert by priority

    return False


def dijkstra(start, target, nodes, open_nodes, closed_nodes):
    """
    Pathfinding algorithm to find shortest path from A to B
    :param start: Start node
    :param target: Target node
    :param nodes: All nodes
    :param open_nodes: Open nodes left unchecked during path resolve
    :param closed_nodes: Checked nodes during path resolve
    :return True if path is found, False if not
    """
    start.h_score = distance(start, target)
    start.f_score = start.h_score
    open_nodes.append(start)

    while open_nodes:
        current = open_nodes.pop(0)
        closed_nodes.append(current)
        initialize_children(current, nodes)

        if current.target:
            return True

        for child in current.children:
            estimate = distance(child, target)
            temp_g_score = current.g_score + child.cost
            temp_f_score = temp_g_score + estimate

            if child in closed_nodes and temp_f_score >= child.f_score:
                continue

            if child not in open_nodes or temp_f_score < child.f_score:
                child.parent = current
                child.f_score = temp_f_score
                child.g_score = temp_g_score
                if child in open_nodes:
                    open_nodes.remove(child)
                
                open_nodes.append(child)
                open_nodes.sort(key = lambda x: x.g_score) # Sort by cost so far, no estimated distance to target
    return False


def bfs(start, target, nodes, open_nodes, closed_nodes):
    """
    Pathfinding algorithm to find shortest path from A to B
    :param start: Start node
    :param target: Target node
    :param nodes: All nodes
    :param open_nodes: Open nodes left unchecked during path resolve
    :param closed_nodes: Checked nodes during path resolve
    :return True if path is found, False if not
    """
    start.h_score = distance(start, target)
    start.f_score = start.h_score
    open_nodes.append(start)

    while open_nodes:
        current = open_nodes.pop(0)
        closed_nodes.append(current)
        initialize_children(current, nodes)

        if current.target:
            return True

        for child in current.children:
            estimate = distance(child, target)
            temp_g_score = current.g_score + child.cost
            temp_f_score = temp_g_score + estimate

            if child in closed_nodes and temp_f_score >= child.f_score:
                continue

            if child not in open_nodes or temp_f_score < child.f_score:
                child.parent = current
                child.f_score = temp_f_score
                child.g_score = temp_g_score
                if child in open_nodes:
                    open_nodes.remove(child)
                
                open_nodes.append(child) # insert last for first in first out

    return False


def initialize_children(current, nodes):
    """
    Fills node.neighbours with all neighbours of 'current'
    :param current: Current node
    :param nodes: All nodes
    """
    for node in nodes:
        if (node.x == current.x + 1 and node.y == current.y) or \
           (node.x == current.x - 1 and node.y == current.y) or \
           (node.x == current.x and node.y == current.y + 1) or \
           (node.x == current.x and node.y == current.y - 1):
            if not node.obstacle:
                current.children.append(node)


def distance(current, target):
    """
    Calculate manhattan distance between current node and target node
    :param current: Current node
    :param target: Target node
    :return manhattan distance
    """
    return abs(target.x - current.x) + abs(target.y - current.y)
