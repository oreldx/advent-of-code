DEBUG = False


def open_input() -> list[list[int]]:
    def parse_line(raw_line: str) -> list:
        ranges = []
        for raw_range in raw_line.strip().split(","):
            boundaries = raw_range.split("-")
            if boundaries[0] == "0" or boundaries[1] == "0":
                print("leading 0 found in the range")
                continue
            ranges.append((int(boundaries[0]), int(boundaries[1])))
        return ranges

    if DEBUG:
        print("DEBUG MODE ON")
        raw_line = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
        return parse_line(raw_line)

    filepath = "input.txt"
    with open(filepath, "r", encoding="utf-8") as f:
        return parse_line(f.readline())


def is_valid_simple_id(given_id: str) -> bool:
    if len(given_id) % 2 != 0:
        return True
    mid_idx = len(given_id) // 2
    return not (given_id[:mid_idx] == given_id[mid_idx:])


def is_valid_sequence_id(given_id: str) -> bool:
    # 1 digit repeat once
    if len(given_id) == 1:
        return True
    mid_idx = len(given_id) // 2
    # seq length is max half total, start from larger to prevent max iters
    for i in range(mid_idx, 0, -1):
        # seq is a modulo total length
        if len(given_id) % i == 0:
            seqs = set()

            # split word in pattern
            for y in range(len(given_id) // i):
                seqs.add(given_id[y * i : (y + 1) * i])
            if len(seqs) == 1:
                return False
    return True


# !NOT MY SOLUTION! I just want to keep in mind this elegant repetition pattern trick
# repeating patterns "wrap around", and duplicating them creates overlapping copies that contain the original string shifted
def is_valid_sequence_id_with_trick(given_id: str) -> bool:
    if len(given_id) <= 1:
        return True
    return given_id not in (given_id + given_id)[1:-1]


def sum_invalids(validator: callable) -> int:
    ids_range = open_input()
    invalid_sum = 0
    for start, end in ids_range:
        for n in range(start, end + 1):
            if not validator(str(n)):
                invalid_sum += n

    return invalid_sum


def problem_1() -> int:
    return sum_invalids(is_valid_simple_id)


def problem_2() -> int:
    return sum_invalids(is_valid_sequence_id)
    # return sum_invalids(is_valid_sequence_id_with_trick)i


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
