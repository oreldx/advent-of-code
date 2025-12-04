from copy import deepcopy

DEBUG = False


def open_input() -> list[list[int]]:
    if DEBUG:
        print("DEBUG MODE ON")
        return (
            [
                [c for c in line]
                for line in [
                    "..@@.@@@@.",
                    "@@@.@.@.@@",
                    "@@@@@.@.@@",
                    "@.@@@@..@.",
                    "@@.@@@@.@@",
                    ".@@@@@@@.@",
                    ".@.@.@.@@@",
                    "@.@@@.@@@@",
                    ".@@@@@@@@.",
                    "@.@.@@@.@.",
                ]
            ],
            [
                "..xx.xx@x.",
                "x@@.@.@.@@",
                "@@@@@.x.@@",
                "@.@@@@..@.",
                "x@.@@@@.@x",
                ".@@@@@@@.@",
                ".@.@.@.@@@",
                "x.@@@.@@@@",
                ".@@@@@@@@.",
                "x.x.@@@.x.",
            ],
        )

    filepath = "input.txt"
    grid = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                return (grid, None)

            line = line.strip()
            grid.append([c for c in line])


def problem_1() -> int:
    (grid, result) = open_input()
    total_count = 0
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if cell != "@":
                continue
            chunk_count = -1
            for n in range(3):
                if i - 1 + n < 0 or i - 1 + n > len(grid) - 1:
                    continue
                for c in grid[i - 1 + n][
                    max(j - 1, 0) : min(j + 1 + 1, len(grid[i - 1 + n]))
                ]:
                    if c == "@":
                        chunk_count += 1
            if chunk_count < 4:
                # display incorrect result compare to awaited one
                if result and result[i][j] != "x":
                    print("cell", cell, i, j, chunk_count)
                    for n in range(3):
                        if i - 1 + n < 0 or i - 1 + n > len(grid) - 1:
                            continue
                        print(
                            grid[i - 1 + n][
                                max(j - 1, 0) : min(j + 1 + 1, len(grid[i - 1 + n]))
                            ]
                        )
                    print("---")
                total_count += 1

    return total_count


def problem_2() -> int:
    def update_grid(grid):
        current_total = 0
        new_grid = deepcopy(grid)
        for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if cell != "@":
                    continue
                chunk_count = -1
                for n in range(3):
                    if i - 1 + n < 0 or i - 1 + n > len(grid) - 1:
                        continue
                    for c in grid[i - 1 + n][
                        max(j - 1, 0) : min(j + 1 + 1, len(grid[i - 1 + n]))
                    ]:
                        if c == "@":
                            chunk_count += 1
                if chunk_count < 4:
                    new_grid[i][j] = "."
                    current_total += 1
        return new_grid, current_total

    (grid, _) = open_input()

    total = 0
    while True:
        grid, iteration_total = update_grid(grid)
        print(iteration_total)
        if iteration_total == 0:
            break
        total += iteration_total

    return total


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
