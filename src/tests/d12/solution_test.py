from src.d12.solution import *
from src.tests.utils.file_stub import FileStub


example = [
    "Sabqponm",
    "abcryxxl",
    "accszExk",
    "acctuvwj",
    "abdefghi",
]


def test_Part1_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = part1(file_stub)

    assert result == "31"


def test_Part2_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = part2(file_stub)

    assert result == "Not solved yet"
