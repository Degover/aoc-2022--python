from src.d10.get_signals import *


def part1(input) -> str:
    sample_cycles = [20, 60, 100, 140, 180, 220]
    all_cycles = get_signals(input)
    cycles_strength = [
        x * cycle for (x, cycle) in all_cycles if cycle in sample_cycles]

    return str(sum(cycles_strength))


def part2(input) -> str:
    return "Not implemented yet"


def solve_d10():
    with open('inputs/10.txt', 'r') as file_input:
        print(part1(file_input))

    with open('inputs/10.txt', 'r') as file_input:
        print(part2(file_input))
