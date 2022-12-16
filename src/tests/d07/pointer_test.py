from src.d07.pointer import *
from src.d07.directory import *


def test_StepIntoAndOut_WithSimpleDirectoryThree_ShouldWorkCorrectly():
    root = Directory("root")
    dir_a = Directory("a")
    dir_b = Directory("b")
    dir_c = Directory("c")
    dir_d = Directory("d")

    dir_c.add_sub_directory(dir_d)
    dir_b.add_sub_directory(dir_c)
    dir_a.add_sub_directory(dir_b)
    root.add_sub_directory(dir_a)

    pointer = Pointer(root)

    assert pointer.current == root

    pointer.step_into("a")
    assert pointer.current == dir_a

    pointer.step_into("b")
    assert pointer.current == dir_b

    pointer.step_into("c")
    assert pointer.current == dir_c

    pointer.step_into("d")
    assert pointer.current == dir_d

    pointer.step_out()
    assert pointer.current == dir_c

    pointer.step_out()
    assert pointer.current == dir_b

    pointer.step_out()
    assert pointer.current == dir_a

    pointer.step_out()
    assert pointer.current == root
