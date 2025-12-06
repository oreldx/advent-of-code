import re

DEBUG = True


def open_input() -> list[list[int]]:
    sample = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]

    filepath = "input.txt"
    data = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = None

            if DEBUG:
                if len(sample) == 0:
                    return data
                line = sample.pop(0)
            else:
                line = f.readline()
                if not line:
                    return data
                line = line.strip()

            line = re.sub(" +", " ", line)
            data.append(line.strip().split(" "))


def apply_operation(sign: str, a: int, b: int) -> int:
    match sign:
        case "*":
            return a * b
        case "+":
            return a + b
        case _:
            raise Exception(f"Unknow sing operator {sign}")


def problem_1() -> int:
    data = open_input()
    operators = data[-1]
    col_results = data[0]
    for row in data[1:-1]:
        for idx, n in enumerate(row):
            col_results[idx] = apply_operation(
                operators[idx], int(n), int(col_results[idx])
            )

    return sum(col_results)


def problem_2() -> int:
    data = open_input()
    operators = data[-1]

    transposed_rows = [[] for _ in range(len(operators))]
    for row in data[0:-1]:
        for i, number in enumerate(row):
            transposed_row = transposed_rows[i]
            for j, digit in enumerate(number):
                if j > len(transposed_row) - 1:
                    transposed_row.append(digit)
                else:
                    transposed_row[j] += digit
            print(transposed_row)

    return None


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
