DEBUG = True


def open_input() -> list[list[int]]:
    def line_parser(bank: str) -> list:
        return [int(c) for c in bank]

    if DEBUG:
        print("DEBUG MODE ON")
        sample = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
        return [line_parser(bank) for bank in sample]

    filepath = "input.txt"
    banks = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                return banks

            line = line.strip()
            banks.append(line_parser(line))


def problem_1() -> int:
    banks = open_input()
    joltageSum = 0
    for bank in banks:
        maximum_ten = max(bank[:-1])
        maximum_unit = max(bank[bank.index(maximum_ten) + 1 :])
        joltageSum += int(f"{maximum_ten}{maximum_unit}")

    return joltageSum


def problem_2() -> int:
    banks = open_input()

    joltageSum = 0
    required_length = 12
    for bank in banks:
        max_joltage = ""
        last_idx = 0
        for i in range(required_length, 0, -1):
            # print(len(bank), i)
            available_range = len(bank) - i
            print(last_idx, available_range + 1)
            maxium = max(bank[last_idx : available_range + 1])
            last_idx = bank[last_idx : available_range + 1].index(maxium) + 1
            max_joltage += str(maxium)

        print(max_joltage)
        joltageSum += int(max_joltage)

    return joltageSum


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
