from src.d07.directory import *
from src.d07.file import *
from src.d07.pointer import *


def parse(input) -> Directory:
    root = Directory("root")
    pointer = Pointer(root)

    important_rows = [row for row in [r.strip() for r in input]
                      if row != "$ cd /" and row != "$ ls" and row != ""]
    for row in important_rows:
        if row.startswith("$ cd"):
            dir_name = row.split(" ")[-1]
            if (dir_name == ".."):
                pointer.step_out()
            else:
                pointer.step_into(dir_name)

        elif row.startswith("dir"):
            pointer.current.add_sub_directory(Directory(row.split(" ")[-1]))

        else:
            [size, name] = row.split(" ")
            pointer.current.add_file(File(name, int(size)))

    return root
