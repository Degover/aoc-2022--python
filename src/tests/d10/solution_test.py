from src.d10.solution import *
from src.tests.utils.file_stub import FileStub
from src.tests.d10.example import example


def test_Part1_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = part1(file_stub)

    assert result == "13140"


def test_Part2_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = part2(file_stub)

    expected = "\n".join([
        "##..##..##..##..##..##..##..##..##..##..",
        "###...###...###...###...###...###...###.",
        "####....####....####....####....####....",
        "#####.....#####.....#####.....#####.....",
        "######......######......######......####",
        "#######.......#######.......#######.....",
    ])
    assert result == expected
