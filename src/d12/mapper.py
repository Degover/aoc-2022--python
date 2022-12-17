from src.d12.node import *
from src.d12.get_height_from import *


class Mapper:
    def __init__(self):
        self.grid: list[list[Node]] = []
        self.unvisited_nodes: list[Node] = []
        self.source: Node = None
        self.target: Node = None

    def read_file_input(self, file_input) -> None:
        for line in file_input:
            self.grid.append([])

            for x, char in enumerate(line):
                if char == '\n':
                    break

                height = get_height_from(char)

                node = Node(height, x, len(self.grid)-1)
                self.grid[-1].append(node)

                if char == "S":
                    self.source = node
                elif char == "E":
                    self.target = node

        self.source.distance = 0

        self.map_node_connections()
        self.unvisited_nodes.append(self.source)

    def map_node_connections(self) -> None:
        for y, row in enumerate(self.grid):
            for x, node in enumerate(row):
                node.connections = []
                if y > 0:
                    up_node = self.grid[y-1][x]
                    if up_node.height <= node.height + 1:
                        node.connections.append(up_node)

                    if node.height <= up_node.height + 1:
                        up_node.connections.append(node)

                if x > 0:
                    left_node = self.grid[y][x-1]
                    if left_node.height <= node.height + 1:
                        node.connections.append(left_node)

                    if node.height <= left_node.height + 1:
                        left_node.connections.append(node)

    def visit_node(self, node: Node) -> None:
        self.unvisited_nodes.remove(node)
        node.was_visited = True

        for connected_node in node.connections:
            if not connected_node.was_visited and not any([connected_node is node for node in self.unvisited_nodes]):
                self.unvisited_nodes.append(connected_node)

            curr_distance = node.distance + 1
            if curr_distance < connected_node.distance:
                connected_node.distance = int(curr_distance)
                connected_node.parent = node

    def calculate_best_route(self) -> int:
        current_node: Node = None

        while len(self.unvisited_nodes) > 0 and current_node is not self.target:
            current_node = min(self.unvisited_nodes)
            self.visit_node(current_node)

        return self.target.distance

    def print_paths(self) -> None:
        '''Debug use only'''
        simple_map = [[(
            node.distance,
            node.parent is not None and node.parent.x > node.x,
            node.parent is not None and node.parent.y > node.y
        ) for node in row] for row in self.grid]

        final_str = ''
        for row in simple_map:
            for i in range(2):
                for distance, is_left, is_above in row:
                    if i == 0:
                        char = 'v' if is_above else ''
                        final_str += f'\t\t{char}'
                    else:
                        char = '>' if is_left else ''
                        final_str += f'\t{char}\t{distance}'
                final_str += '\n'
            final_str += '\n'

        print(final_str)
