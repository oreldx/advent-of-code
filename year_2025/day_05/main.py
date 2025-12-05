DEBUG = False


def open_input() -> list[list[int]]:
    sample = [
        "3-5",
        "10-14",
        "16-20",
        "12-18",
        "",
        "1",
        "5",
        "8",
        "11",
        "17",
        "32",
    ]

    filepath = "input.txt"
    data = {"ranges": [], "ids": [], "max_range_idx": 0}
    ranges_done = False
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

            if line == "":
                ranges_done = True
                continue

            if ranges_done:
                data["ids"].append(int(line))
                continue
            parsed_range = [int(n) for n in line.split("-")]
            data["max_range_idx"] = max([data["max_range_idx"]] + parsed_range)
            data["ranges"].append(parsed_range)


def problem_1() -> int:
    data = open_input()

    fresh_range = [False for _ in range(data["max_range_idx"] + 1)]
    for r in data["ranges"]:
        print(r)
        for i in range(r[0], r[1] + 1):
            fresh_range[i] = True

    return sum(
        [1 if idx < len(fresh_range) and fresh_range[idx] else 0 for idx in data["ids"]]
    )


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
