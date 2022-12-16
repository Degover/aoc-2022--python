from src.d07.directory import *
from src.d07.file import *
from src.d07.input_parser import *
from src.d07.pointer import *
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


def test_Parse_WithExample_ShouldParseCorrectly():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = parse(file_stub)

    expected = (
        Directory("root")
        .add_file(File("b.txt", 14848514))
        .add_file(File("c.dat", 8504156))
        .add_sub_directory(
            Directory("a")
            .add_file(File("f", 29116))
            .add_file(File("g", 2557))
            .add_file(File("h.lst", 62596))
            .add_sub_directory(
                Directory("e")
                .add_file(File("i", 584))
            )
        )
        .add_sub_directory(
            Directory("d")
            .add_file(File("j", 4060174))
            .add_file(File("d.log", 8033020))
            .add_file(File("d.ext", 5626152))
            .add_file(File("k", 7214296))
        )
    )

    assert result == expected
