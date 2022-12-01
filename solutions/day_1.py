from helper import load_input


def process_input(data: str):
    split_data = data.split("\n")
    elves = []
    elf = []
    last_item = split_data[-1]
    for s in split_data:
        if s == last_item:
            elf.append(int(s))
            elves.append(elf)
        elif s != "":
            elf.append(int(s))
        else:
            elves.append(list(elf))
            elf.clear()
    return elves


def solution(data: str) -> int:
    elves = process_input(data)
    calories_sum = []
    for elf in elves:
        calories_sum.append(sum(elf))

    calories_sum.sort(reverse=True)
    return calories_sum[0], sum(calories_sum[:3])


if __name__ == "__main__":
    data = load_input()
    res = solution(data)
    print(res)
