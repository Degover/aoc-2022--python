from src.d10.get_signals import *


def part1(input) -> str:
    sample_cycles = [20, 60, 100, 140, 180, 220]
    all_cycles = get_signals(input)
    cycles_strength = [
        x * cycle for (x, cycle) in all_cycles if cycle in sample_cycles]

    return str(sum(cycles_strength))


def part2(input) -> str:
    all_cycles = get_signals(input)
    test = [
        "#" if x-1 <= (cycle-1) % 40 <= x+1 else "."
        for (x, cycle) in all_cycles
    ]

    return "\n".join([
        "".join(test[:40]),
        "".join(test[40:80]),
        "".join(test[80:120]),
        "".join(test[120:160]),
        "".join(test[160:200]),
        "".join(test[200:]),
    ])


def solve_d10():
    with open('inputs/10.txt', 'r') as file_input:
        print(part1(file_input))

    with open('inputs/10.txt', 'r') as file_input:
        print(part2(file_input))
