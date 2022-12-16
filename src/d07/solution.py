from src.d07.input_parser import *
from src.d07.directory import *


def part1(input) -> str:
    root = parse(input)
    all_dirs = flat_dir_list(root.sub_directories)
    dirs_sizes = [dir.get_total_size() for dir in all_dirs]
    result = sum([size for size in dirs_sizes if size <= 100_000])
    return str(result)


total_fylesystem_size = 70_000_000
update_size = 30_000_000


def part2(input) -> str:
    root = parse(input)

    free_space = total_fylesystem_size - root.get_total_size()
    required_space = update_size - free_space

    all_dirs = flat_dir_list(root.sub_directories)
    dirs_sizes = [dir.get_total_size() for dir in all_dirs]
    result = min([size for size in dirs_sizes if size >= required_space])
    return str(result)


def flat_dir_list(dir_list: list[Directory]) -> list[Directory]:
    sub_dirs = [flat_dir_list(dir.sub_directories)
                for dir in dir_list if dir.sub_directories != []]
    return [item for sublist in sub_dirs for item in sublist] + dir_list


def solve_d7():
    with open('inputs/7.txt', 'r') as file_input:
        print(part1(file_input))

    with open('inputs/7.txt', 'r') as file_input:
        print(part2(file_input))
