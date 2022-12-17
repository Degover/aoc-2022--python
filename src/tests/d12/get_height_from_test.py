from src.d12.get_height_from import *


def test_GetHeightFrom_WithNormalSample_ShouldBeCorrect():
    assert get_height_from("a") == 0
    assert get_height_from("b") == 1
    assert get_height_from("c") == 2

    assert get_height_from("h") == 7
    assert get_height_from("i") == 8
    assert get_height_from("j") == 9

    assert get_height_from("p") == 15
    assert get_height_from("q") == 16
    assert get_height_from("r") == 17

    assert get_height_from("x") == 23
    assert get_height_from("y") == 24
    assert get_height_from("z") == 25


def test_GetHeightFrom_WithStartAndEndPoints_ShouldBeCorrect():
    assert get_height_from("S") == 0
    assert get_height_from("E") == 25
