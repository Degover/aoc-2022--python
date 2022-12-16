from src.d10.solution import *
from src.tests.utils.file_stub import FileStub


def test_Part1_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array([])

    result = part1(file_stub)

    assert result == "Not solved yet"


def test_Part2_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array([])

    result = part2(file_stub)

    assert result == "Not solved yet"
