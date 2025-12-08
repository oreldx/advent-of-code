DEBUG = False


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
    def create_box_index(t: list) -> str:
        return "-".join([str(d) for d in t])

    data = open_input()

    unique_paires = {}
    for idx, i in enumerate(data[:-1]):
        for j in data[:idx] + data[idx + 1 :]:
            if (create_box_index(j) + create_box_index(i)) in unique_paires:
                continue
            unique_key = create_box_index(i) + create_box_index(j)

            unique_paires[unique_key] = {
                "a": i,
                "b": j,
                "d": (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2,
            }

    paires = unique_paires.values()
    shortest_distances = sorted(paires, key=lambda d: d["d"])

    def find_group_idx(box_id: str, groups: list) -> int:
        for idx, g in enumerate(groups):
            if box_id in g:
                return idx
        return -1

    groups = []
    boxes = set()

    requiered_connections = 10
    if DEBUG:
        requiered_connections = 1000

    for idx, d in enumerate(shortest_distances[:requiered_connections]):
        if len(data) == len(boxes):
            break
        box_0_idx = create_box_index(d["a"])
        box_1_idx = create_box_index(d["b"])

        # both points have already been visited
        if box_0_idx in boxes and box_1_idx in boxes:
            box_group_0_idx = find_group_idx(box_0_idx, groups)
            box_group_1_idx = find_group_idx(box_1_idx, groups)
            if box_group_0_idx == box_group_1_idx:
                # Same edge visited (opposite direction)
                continue

            groups[box_group_0_idx] = groups[box_group_0_idx].union(
                groups[box_group_1_idx]
            )
            groups.pop(box_group_1_idx)

            continue

        # of one the point has been visited to the related point is connected
        if box_0_idx in boxes:
            boxes.add(box_1_idx)
            box_group_0_idx = find_group_idx(box_0_idx, groups)
            groups[box_group_0_idx].add(box_1_idx)
            continue

        if box_1_idx in boxes:
            boxes.add(box_0_idx)
            box_group_1_idx = find_group_idx(box_1_idx, groups)
            groups[box_group_1_idx].add(box_0_idx)
            continue

        # edge not found
        boxes.add(box_0_idx)
        boxes.add(box_1_idx)
        groups.append(set([box_0_idx, box_1_idx]))

    sumt = 1
    for n in sorted([len(g) for g in groups], reverse=True)[:3]:
        sumt *= n

    return sumt


def problem_2() -> int:
    def create_box_index(t: list) -> str:
        return "-".join([str(d) for d in t])

    data = open_input()

    unique_paires = {}
    for idx, i in enumerate(data[:-1]):
        for j in data[:idx] + data[idx + 1 :]:
            if (create_box_index(j) + create_box_index(i)) in unique_paires:
                continue
            unique_key = create_box_index(i) + create_box_index(j)

            unique_paires[unique_key] = {
                "a": i,
                "b": j,
                "d": (i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2 + (i[2] - j[2]) ** 2,
            }

    paires = unique_paires.values()
    shortest_distances = sorted(paires, key=lambda d: d["d"])

    def find_group_idx(box_id: str, groups: list) -> int:
        for idx, g in enumerate(groups):
            if box_id in g:
                return idx
        return -1

    groups = []
    boxes = set()

    longest = None
    for idx, d in enumerate(shortest_distances):
        if len(boxes) == len(data) and len(groups) == 1:
            longest = shortest_distances[idx - 1]
            break
        box_0_idx = create_box_index(d["a"])
        box_1_idx = create_box_index(d["b"])

        # both points have already been visited
        if box_0_idx in boxes and box_1_idx in boxes:
            box_group_0_idx = find_group_idx(box_0_idx, groups)
            box_group_1_idx = find_group_idx(box_1_idx, groups)
            if box_group_0_idx == box_group_1_idx:
                # Same edge visited (opposite direction)
                continue

            groups[box_group_0_idx] = groups[box_group_0_idx].union(
                groups[box_group_1_idx]
            )
            groups.pop(box_group_1_idx)

            continue

        # of one the point has been visited to the related point is connected
        if box_0_idx in boxes:
            boxes.add(box_1_idx)
            box_group_0_idx = find_group_idx(box_0_idx, groups)
            groups[box_group_0_idx].add(box_1_idx)
            continue

        if box_1_idx in boxes:
            boxes.add(box_0_idx)
            box_group_1_idx = find_group_idx(box_1_idx, groups)
            groups[box_group_1_idx].add(box_0_idx)
            continue

        # edge not found
        boxes.add(box_0_idx)
        boxes.add(box_1_idx)
        groups.append(set([box_0_idx, box_1_idx]))

    return longest["a"][0] * longest["b"][0]


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
