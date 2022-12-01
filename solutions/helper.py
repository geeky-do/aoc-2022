def load_input() -> str:
    file_input = ""
    with open("input.txt") as reader:
        file_input += reader.read()
    return file_input
