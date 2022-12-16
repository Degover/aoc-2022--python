from src.d07.directory import *


def test_GetTotalSize_WithDirectoryThree_ShouldBeCorrect():
    root = (
        Directory("root")
        .add_file(File("root_a", 5))
        .add_file(File("root_b", 10))
        .add_file(File("root_c", 15))
        .add_sub_directory(
            Directory("1")
            .add_file(File("1_a", 10))
            .add_file(File("1_b", 10)))
        .add_sub_directory(
            Directory("2")
            .add_file(File("2_a", 20))
            .add_file(File("2_b", 25))
            .add_sub_directory(
                Directory("3")
                .add_file(File("3_a", 20))
                .add_file(File("3_b", 25))
                .add_file(File("3_c", 100)))))

    result = root.get_total_size()

    assert result == 240
