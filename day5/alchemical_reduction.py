with open("input5.txt") as f:
    line = ''.join(f.readlines())


def units_after_reaction(polymer):
    i = 0
    while i < len(polymer) - 1:
        if (polymer[i].lower() == polymer[i + 1].lower() and
                polymer[i] != polymer[i + 1]):
            polymer = polymer[:i] + polymer[i + 2:]
            if i > 0:
                i -= 1
            continue
        i += 1
    return len(polymer)


def shortest_polymer(polymer):
    shortest = len(polymer)
    for x in set(polymer.lower()):
        n = polymer.count(x) - polymer.count(x.upper())
        new_polymer = ''.join([c for c in polymer if c != x and c != x.upper()])
        new_polymer_length = units_after_reaction(new_polymer) + n
        if new_polymer_length < shortest:
            shortest = new_polymer_length
    return shortest


if __name__ == "__main__":
    print(units_after_reaction(line))
    print(shortest_polymer(line))
