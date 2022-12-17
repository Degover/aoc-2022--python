alphabet = "abcdefghijklmnopqrstuvwxyz"
height_values = {char: index for (index, char) in enumerate(alphabet)}

height_values["E"] = height_values["z"]
height_values["S"] = height_values["a"]


def get_height_from(char: str) -> int:
    return height_values[char]
