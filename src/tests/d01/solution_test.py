import unittest
from src.d01.solution import *
from src.tests.utils.file_stub import *

tc = unittest.TestCase()
example = [
    "1000",
    "2000",
    "3000",
    "",
    "4000",
    "",
    "5000",
    "6000",
    "",
    "7000",
    "8000",
    "9000",
    "",
    "10000",
]


def test_Part1_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = part1(file_stub)

    tc.assertEqual(result, "24000")


def test_Part2_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = part2(file_stub)

    tc.assertEqual(result, "45000")
