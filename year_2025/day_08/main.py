import math

DEBUG = True


def open_input() -> list[list[int]]:
    sample = [
        "162,817,812",
        "57,618,57",
        "906,360,560",
        "592,479,940",
        "352,342,300",
        "466,668,158",
        "542,29,236",
        "431,825,988",
        "739,650,466",
        "52,470,668",
        "216,146,977",
        "819,987,18",
        "117,168,530",
        "805,96,715",
        "346,949,466",
        "970,615,88",
        "941,993,340",
        "862,61,35",
        "984,92,344",
        "425,690,689",
    ]

    filepath = "input.txt"
    space = []
    with open(filepath, "r", encoding="utf-8") as f:
        while True:
            line = None

            if DEBUG:
                if len(sample) == 0:
                    return space
                line = sample.pop(0)
            else:
                line = f.readline()
                if not line:
                    return space
                line = line.strip()

            space.append([int(c) for c in line.split(",")])


def problem_1() -> int:
    data = open_input()

    required_connections = 1000
    if DEBUG:
        required_connections = 10

    distances = []
    for idx, i in enumerate(data[:-1]):
        for j in data[:idx] + data[idx + 1 :]:
            distances.append(
                {
                    "boxes": [i, j],
                    "d": math.sqrt(
                        (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[1] - j[1]) ** 2
                    ),
                }
            )
    shortest_distances = sorted(distances, key=lambda d: d["d"])

    def find_group_idx(box_id: str, groups: list) -> int:
        for idx, g in enumerate(groups):
            if box_id in g:
                return idx
        return -1

    groups = []
    boxes = set()
    for d in shortest_distances:
        box_0_idx = "-".join([str(d) for d in d["boxes"][0]])
        box_1_idx = "-".join([str(d) for d in d["boxes"][1]])
        if box_0_idx in boxes and box_1_idx in boxes:
            box_group_0_idx = find_group_idx(box_0_idx, groups)
            box_group_1_idx = find_group_idx(box_1_idx, groups)
            if box_group_0_idx == box_group_1_idx:
                continue

            groups[box_group_0_idx] = groups[box_group_0_idx].union(
                groups[box_group_1_idx]
            )
            groups.pop(box_group_1_idx)

            continue

        if box_0_idx in boxes:
            boxes.add(box_1_idx)
            for g in groups:
                if box_0_idx in g:
                    g.add(box_1_idx)
                    break
            continue

        if box_1_idx in boxes:
            boxes.add(box_0_idx)
            for g in groups:
                if box_1_idx in g:
                    g.add(box_0_idx)
                    break
            continue

        boxes.add(box_0_idx)
        boxes.add(box_1_idx)
        groups.append(set([box_0_idx, box_1_idx]))

        if len(data) == len(boxes):
            break

    print(groups)
    for g in groups:
        print(len(g))

    return 0


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
