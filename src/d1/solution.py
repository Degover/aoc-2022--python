from src.d1.input_parser import *


def part1(file_input):
    return str(parse_calories_per_elf(file_input)[0])


def part2(file_input):
    return str(sum(parse_calories_per_elf(file_input)[0:3]))


def solve_d1():
    with open('inputs/1.txt', 'r') as file_input:
        print(part1(file_input))

    with open('inputs/1.txt', 'r') as file_input:
        print(part2(file_input))
