import math

DEBUG = False


def open_input() -> list[list[int]]:
    if DEBUG:
        print("DEBUG MODE ON")
        return [
            "L68",
            "L30",
            "R48",
            "L5",
            "R60",
            "L55",
            "L1",
            "L99",
            "R14",
            "L82",
        ]

    filepath = "input.txt"
    rotations = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = f.readline()
            if not line:
                return rotations

            line = line.replace("\n", "")
            rotations.append(line)


def apply_rotation(raw_inst: str, current_pos: int, max_dial=100) -> int:
    def get_sign(direction: str) -> int:
        match direction:
            case "L":
                return -1
            case "R":
                return 1
            case _:
                raise Exception("Unknow direction")

    return (current_pos + get_sign(raw_inst[0]) * int(raw_inst[1:])) % max_dial


def problem_1() -> int:
    rotations = open_input()

    pwd = 0
    dial_pos = 50
    for r in rotations:
        dial_pos = apply_rotation(r, dial_pos)
        if dial_pos == 0:
            pwd += 1

    return pwd


def apply_rotation_and_count(raw_inst: str, current_pos: int, max_dial=100) -> int:
    def get_sign(direction: str) -> int:
        match direction:
            case "L":
                return -1
            case "R":
                return 1
            case _:
                raise Exception("Unknow direction")

    new_pos_absolute = current_pos + get_sign(raw_inst[0]) * int(raw_inst[1:])

    count = math.floor(abs(new_pos_absolute) / (max_dial))
    # going backward passing 0
    if current_pos > 0 and new_pos_absolute < 0:
        count += 1
    new_pos_relative = new_pos_absolute % max_dial
    # stopping on 0 shouldn't add count
    if new_pos_relative == 0 and count > 0:
        count -= 1

    return new_pos_relative, count


def problem_2() -> int:
    rotations = open_input()

    pwd = 0
    dial_pos = 50
    for r in rotations:
        (dial_pos, count) = apply_rotation_and_count(r, dial_pos)
        print(dial_pos, count)

        pwd += count
        if dial_pos == 0:
            pwd += 1

    return pwd


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
