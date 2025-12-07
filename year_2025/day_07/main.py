DEBUG = False


def open_input_1() -> list[list[int]]:
    sample = [
        ".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "...............",
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

            grid.append([c for c in line.strip()])


def print_grid(grid: list) -> None:
    for row in grid:
        line = ""
        for cell in row:
            line += cell
        print(line)


def problem_1() -> int:
    data = open_input_1()
    split_count = 0

    # consideration: all bim splitters are always min 1 unit away from each other
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell in ["S", "|"]:
                if i + 1 < len(data) and data[i + 1][j] == ".":
                    data[i + 1][j] = "|"
            if cell == "^":
                if data[i - 1][j] == "|":
                    data[i][j - 1] = "|"
                    data[i][j + 1] = "|"
                    data[i + 1][j - 1] = "|"
                    data[i + 1][j + 1] = "|"
                    split_count += 1

    return split_count


def problem_2() -> int:
    data = open_input_1()
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell in ["S", "|"]:
                if i + 1 < len(data) and data[i + 1][j] == ".":
                    data[i + 1][j] = "|"
            if cell == "^":
                if data[i - 1][j] == "|":
                    data[i][j - 1] = "|"
                    data[i][j + 1] = "|"
                    data[i + 1][j - 1] = "|"
                    data[i + 1][j + 1] = "|"

    counter = 0
    for i in range(0, len(data), 2):
        for j in range(len(data[i])):
            if data[i][j] == "|" and data[i + 1][j] == "|":
                counter += 1

    return counter


def main() -> None:
    if DEBUG:
        print(problem_2())
        return

    match input("Choose which problem to print (1 or 2): "):
        case "1":
            print(problem_1())
        case "2":
            print(problem_2())
        case _:
            print("Invalid choice. Please enter 1 or 2.")


main()
