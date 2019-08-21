from collections import Counter

with open("input2.txt") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]


def calculate_checksum(box_ids):
    two_count = 0
    three_count = 0
    for id in box_ids:
        count = Counter(id).values()
        two_count += 2 in count
        three_count += 3 in count
    return two_count * three_count


def common_letters(box_ids):
    for box1 in box_ids:
        for box2 in box_ids:
            common = ''.join(a for a, b in zip(box1, box2) if a == b)
            if len(common) == len(box1) - 1:
                return common


if __name__ == "__main__":
    print(calculate_checksum(lines))
    print(common_letters(lines))
