from helper import load_input


def process_input(raw_elf_calories: str) -> list[list[str]]:
    calories = raw_elf_calories.split("\n\n")
    elf_calories = [list(filter(None, elf.split("\n"))) for elf in calories]

    return elf_calories


def aggregate_calories(elf_calories: list[list[str]]) -> list[int]:
    return [sum(int(item) for item in calories) for calories in elf_calories]


def solution(data: str) -> int:
    elves = process_input(data)
    calories_sum = aggregate_calories(elves)

    calories_sum.sort(reverse=True)
    return calories_sum[0], sum(calories_sum[:3])


if __name__ == "__main__":
    data = load_input()
    res = solution(data)
    print(res)
