from src.d07.solution import *
from src.tests.utils.file_stub import FileStub

example = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]


def test_Part1_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = part1(file_stub)

    assert result == "95437"


def test_Part2_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = part2(file_stub)

    assert result == "24933642"
