class File:
    def __init__(self, name: str, size: int):
        self.name: str = name
        self.size: int = size

    def __eq__(self, obj):
        if not isinstance(obj, File):
            return False

        return obj.name == self.name and obj.size == self.size
