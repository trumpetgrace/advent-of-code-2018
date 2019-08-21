import re
from collections import Counter

with open("input3.txt") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]


def overlapping_claims(claims):
    claimed_coords = []
    for claim in claims:
        claim = re.sub("#\\d+ @ ", "", claim)
        x, y = list(map(int, claim.split()[0].replace(":", "").split(",")))
        width, height = list(map(int, claim.split()[1].split("x")))
        for i in range(width):
            for j in range(height):
                coord = (x + i, y + j)
                claimed_coords.append(coord)
    count = Counter(claimed_coords)
    return sum(1 for coord in count.values() if coord > 1)


def intact_claim(claims):
    claimed_coords = []
    for claim in claims:
        claim = re.sub("#\\d+ @ ", "", claim)
        x, y = list(map(int, claim.split()[0].replace(":", "").split(",")))
        width, height = list(map(int, claim.split()[1].split("x")))
        for i in range(width):
            for j in range(height):
                coord = (x + i, y + j)
                claimed_coords.append(coord)
    count = Counter(claimed_coords)
    for claim in claims:
        overlapping = False
        id = re.search("#(\\d+)", claim).group(1)
        claim = re.sub("#\\d+ @ ", "", claim)
        x, y = list(map(int, claim.split()[0].replace(":", "").split(",")))
        width, height = list(map(int, claim.split()[1].split("x")))
        for i in range(width):
            for j in range(height):
                coord = (x + i, y + j)
                if count[coord] > 1:
                    overlapping = True
        if not overlapping:
            return int(id)


if __name__ == "__main__":
    print(overlapping_claims(lines))
    print(intact_claim(lines))
