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
    data = {
        "ranges": [],
        "ids": [],
    }
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
            data["ranges"].append(parsed_range)


def problem_1() -> int:
    data = open_input()

    fresh_ids_count = 0
    for n in data["ids"]:
        for r in data["ranges"]:
            if n >= r[0] and n <= r[1]:
                fresh_ids_count += 1
                break

    return fresh_ids_count


def optimize_ranges(prev_ranges: list) -> list:
    new_ranges = []
    for prev_range in prev_ranges:
        # update_new_ranges(new_ranges, pr)
        hasOverlapped = False
        for new_range in new_ranges:
            if prev_range[0] > new_range[1] or prev_range[1] < new_range[0]:
                # no overlapping at all
                continue
            if prev_range[0] < new_range[0] and prev_range[1] >= new_range[0]:
                # prev range start earlier
                new_range[0] = prev_range[0]
            if prev_range[1] > new_range[1] and prev_range[0] <= new_range[1]:
                # prev range end later
                new_range[1] = prev_range[1]
            hasOverlapped = True
        if not hasOverlapped:
            new_ranges.append(prev_range)

    return new_ranges


def problem_2() -> int:
    data = open_input()

    original_ranges = data["ranges"]
    opti_ranges = original_ranges
    while True:
        opti_ranges = optimize_ranges(original_ranges)
        if len(opti_ranges) == len(original_ranges):
            break
        original_ranges = opti_ranges
    possibles = 0
    for r in opti_ranges:
        possibles += r[1] - r[0] + 1

    return possibles


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
