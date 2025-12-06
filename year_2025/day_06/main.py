import re

DEBUG = False


def open_input_1() -> list[list[int]]:
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
    data = open_input_1()
    operators = data[-1]
    col_results = data[0]
    for row in data[1:-1]:
        for idx, n in enumerate(row):
            col_results[idx] = apply_operation(
                operators[idx], int(n), int(col_results[idx])
            )

    return sum(col_results)


def open_input_2() -> list[list[int]]:
    sample = [
        "123 328  51 64 ",
        " 45 64  387 23 ",
        "  6 98  215 314",
        "*   +   *   +  ",
    ]

    filepath = "input.txt"
    lines = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = None

            if DEBUG:
                if len(sample) == 0:
                    return lines
                line = sample.pop(0)
            else:
                line = f.readline()
                if not line:
                    return lines
                line = line.replace("\n", "")

            lines.append(line)

    return lines


def problem_2() -> int:
    raw_data = open_input_2()

    total_sum = 0
    current_operation = []
    for i in range(len(raw_data[0]), 0, -1):
        col_n = ""
        for j in range(len(raw_data) - 1):
            if raw_data[j][i - 1] == " ":
                continue
            col_n += raw_data[j][i - 1]
        if col_n != "":
            current_operation.append(int(col_n))
        if raw_data[-1][i - 1] in ["*", "+"]:
            current_operation_sing = raw_data[-1][i - 1]
            res = int(current_operation[0])
            for n in current_operation[1:]:
                res = apply_operation(current_operation_sing, res, int(n))
            current_operation = []
            total_sum += res

    return total_sum


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
