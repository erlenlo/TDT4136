class Node:
    """
    One nodein the given board.
    """
    def __init__(self, x, y, cost, obstacle=False, description=None):
        self.x = x
        self.y = y
        self.children = []
        self.parent = None
        self.f_score = float('inf')     # g_score + h_score
        self.g_score = 0                # Cost for this path so far
        self.h_score = 0                # Estimated distance to target.
        self.description = description
        self.obstacle = obstacle        # boolean
        self.start = False              # boolean
        self.target = False             # boolean
        self.cost = cost                


    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.f_score  < other.f_score

    def __str__(self):
        return str(self.x) + ' ' + str(self.y)

    def __repr__(self):
        return str(self.x) + ' ' + str(self.y)
