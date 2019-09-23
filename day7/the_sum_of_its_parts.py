from collections import defaultdict

with open("input7.txt") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]


def order_of_steps(instructions):
    order_dict = defaultdict(list)
    for instruction in instructions:
        instruction = instruction.split(" ")
        order_dict[instruction[7]].append(instruction[1])
        if instruction[1] not in order_dict:
            order_dict[instruction[1]] = []
    order = ""
    while len(order_dict.keys()) != 0:
        min_keys = []
        for key in order_dict.keys():
            if len(order_dict[key]) == 0:
                min_keys.append(key)
        next_key = min(min_keys)
        order += next_key
        for key in list(order_dict.keys()):
            if len(order_dict[key]) == 0 and key in order:
                del order_dict[key]
                continue
            if next_key in order_dict[key]:
                order_dict[key].remove(next_key)
    return order


def time_to_complete_steps(instructions, workers, simple):
    order_dict = defaultdict(list)
    for instruction in instructions:
        instruction = instruction.split(" ")
        order_dict[instruction[7]].append(instruction[1])
        if instruction[1] not in order_dict:
            order_dict[instruction[1]] = []
    order_dict = sorted(order_dict.items())
    time = 0
    in_progress = {}
    completed = []
    while len(completed) != len(order_dict):
        for instruction, dependencies in order_dict:
            if instruction not in completed and instruction not in in_progress and all(i in completed for i in dependencies):
                if simple:
                    in_progress[instruction] = ord(instruction) - 64
                else:
                    in_progress[instruction] = ord(instruction) - 4
                if len(in_progress) == workers:
                    break
        next = min(in_progress.values())
        time += next
        for i in in_progress:
            in_progress[i] -= next
            if in_progress[i] == 0:
                completed.append(i)
        for i in completed:
            if i in in_progress:
                del in_progress[i]
    return time


if __name__ == "__main__":
    print(order_of_steps(lines))
    print(time_to_complete_steps(lines, 5, False))
