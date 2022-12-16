from src.d07.directory import *


class Pointer:
    def __init__(self, root: Directory):
        self.current = root
        self._previous: list[Directory] = []

    def step_into(self, dir_name: str):
        selected_dir = [
            dir for dir in self.current.sub_directories if dir.name == dir_name
        ][0]
        self._previous.append(self.current)
        self.current = selected_dir

    def step_out(self):
        self.current = self._previous.pop()
