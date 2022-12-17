from functools import total_ordering


@total_ordering
class Node:

    def __init__(self, height: int, x: int = 0, y: int = 0):
        self.height: int = height
        self.distance: int = float('inf')
        self.parent: Node | None = None
        self.connections: list[Node] = []
        self.was_visited = False
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return self is other

    def __repr__(self):
        return f'<({self.x}, {self.y}): {self.height}>'
