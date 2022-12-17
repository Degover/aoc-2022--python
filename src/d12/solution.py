from src.d12.mapper import *


def part1(input) -> str:
    mapper = Mapper()
    mapper.read_file_input(input)
    result = mapper.calculate_best_route()
    return str(result)


def part2(input) -> str:
    return "Not solved yet"


def solve_d12():
    with open('inputs/12.txt', 'r') as file_input:
        print(part1(file_input))

    with open('inputs/12.txt', 'r') as file_input:
        print(part2(file_input))
