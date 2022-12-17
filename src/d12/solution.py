from src.d12.mapper import *


def part1(input) -> str:
    mapper = Mapper()
    mapper.read_file_input(input)
    result = mapper.calculate_best_route()
    return str(result)


def part2(input) -> str:
    mapper = Mapper()
    mapper.is_source = lambda char: char == "E"
    mapper.is_target = lambda char: char == "a"
    mapper.can_connect = lambda from_node, to_node: from_node.height <= to_node.height + 1

    mapper.read_file_input(input)
    mapper.calculate_best_route()

    result = min([
        node.distance
        for line in mapper.grid
        for node in line
        if node.height == 0
    ])

    return str(result)


def solve_d12():
    with open('inputs/12.txt', 'r') as file_input:
        print(part1(file_input))

    with open('inputs/12.txt', 'r') as file_input:
        print(part2(file_input))
