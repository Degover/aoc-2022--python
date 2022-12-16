from src.d07.file import *


class Directory:
    def __init__(self, name: str):
        self.name: str = name
        self.files: list[File] = []
        self.sub_directories: list['Directory'] = []

    def add_file(self, file: File) -> 'Directory':
        self.files.append(file)
        return self

    def add_sub_directory(self, directory: 'Directory') -> 'Directory':
        self.sub_directories.append(directory)
        return self

    def get_total_size(self) -> int:
        file_size = sum([file.size for file in self.files])
        dirs_size = sum([dir.get_total_size() for dir in self.sub_directories])
        return file_size + dirs_size

    def __eq__(self, obj):
        if not isinstance(obj, Directory):
            return False

        return obj.files == self.files and obj.sub_directories == self.sub_directories
