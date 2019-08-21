with open("input1.txt") as f:
    lines = f.readlines()
lines = [int(x.strip()) for x in lines]


def resulting_frequency(freq):
    return sum(freq)


def repeated_frequency(freq):
    f = 0
    res_freq = {f}
    while True:
        for x in freq:
            f += x
            if f in res_freq:
                return f
            res_freq.add(f)


if __name__ == "__main__":
    print(resulting_frequency(lines))
    print(repeated_frequency(lines))
