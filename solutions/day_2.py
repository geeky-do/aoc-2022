from helper import load_input


def process_input(input: str):
    return [i.replace(" ", "") for i in input.strip().split("\n")]


def solution(rounds):
    outcomes = {
        "AX": 4,
        "AY": 8,
        "AZ": 3,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 7,
        "CY": 2,
        "CZ": 6,
    }

    total_score_p1 = 0
    for round in rounds:
        total_score_p1 += outcomes[round]

    # DESIRED OUTCOMES
    # Changed the values of the outcomes depending on the rules
    # X = LOSS, Y = DRAW, Z = WIN
    # (got values looking at table above)
    desired_outcomes = {
        "AX": 3,
        "AY": 4,
        "AZ": 8,
        "BX": 1,
        "BY": 5,
        "BZ": 9,
        "CX": 2,
        "CY": 6,
        "CZ": 7,
    }

    total_score_p2 = 0
    for round in rounds:
        total_score_p2 += desired_outcomes[round]

    # Answers
    print("Answer to part 1: ", total_score_p1)
    print("Answer to part 2: ", total_score_p2)


if __name__ == "__main__":
    data = load_input()
    rounds = process_input(data)
    solution(rounds)
