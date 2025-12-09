DEBUG = False


def open_input() -> list[list[int]]:
    sample = [
        "7,1",
        "11,1",
        "11,7",
        "9,7",
        "9,5",
        "2,5",
        "2,3",
        "7,3",
    ]

    filepath = "input.txt"
    grid = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = None

            if DEBUG:
                if len(sample) == 0:
                    return grid
                line = sample.pop(0)
            else:
                line = f.readline()
                if not line:
                    return grid
                line = line.strip()

            grid.append([int(c) for c in line.split(",")])


def problem_1() -> int:
    data = open_input()
    areas = set()
    for idx_i, i in enumerate(data):
        for j in data[:idx_i] + data[idx_i + 1 :]:
            areas.add((abs(i[0] - j[0]) + 1) * (abs(i[1] - j[1]) + 1))

    return max(areas)


def problem_2() -> int:
    data = open_input()
    return 0


def main() -> None:
    if DEBUG:
        print(problem_1())
        return

    match input("Choose which problem to print (1 or 2): "):
        case "1":
            print(problem_1())
        case "2":
            print(problem_2())
        case _:
            print("Invalid choice. Please enter 1 or 2.")


main()
