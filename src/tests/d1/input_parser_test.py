from src.d1.input_parser import *
from src.tests.utils.file_stub import *


def test_ParseCaloriesPerElf_ShouldParseCorrecly():
    file_stub = FileStub()
    file_stub.set_array([
        "1000", "2000", "3000", "", "4000", "", "5000", "6000", "", "7000", "8000", "9000", "",
        "10000",
    ])

    result = list(parse_calories_per_elf(file_stub))

    expected = [24000, 11000, 10000, 6000, 4000]
    assert result == expected
