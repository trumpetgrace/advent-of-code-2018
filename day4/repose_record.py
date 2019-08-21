from collections import defaultdict, Counter
from datetime import datetime, timedelta
import re

with open("input4.txt") as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]


def strategy_1(records):
    records = sorted(records)
    guards = defaultdict(list)
    guard_id = 0
    time_asleep = 0
    for record in records:
        if "Guard" in record:
            guard_id = int(re.search("Guard #(\\d+)", record).group(1))
        elif "asleep" in record:
            time_asleep = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', record)
            time_asleep = datetime.strptime(time_asleep.group(), '%Y-%m-%d %H:%M')
        elif "wakes" in record:
            time_awake = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', record)
            time_awake = datetime.strptime(time_awake.group(), '%Y-%m-%d %H:%M')
            while time_asleep < time_awake:
                guards[guard_id].append(time_asleep.minute)
                time_asleep += timedelta(minutes=1)
            time_asleep = 0
    max_key = max(guards, key=lambda x: len(guards[x]))
    return max_key * Counter(guards[max_key]).most_common(1)[0][0]


def strategy_2(records):
    records = sorted(records)
    guards = defaultdict(list)
    guard_id = 0
    time_asleep = 0
    for record in records:
        if "Guard" in record:
            guard_id = int(re.search("Guard #(\\d+)", record).group(1))
        elif "asleep" in record:
            time_asleep = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', record)
            time_asleep = datetime.strptime(time_asleep.group(), '%Y-%m-%d %H:%M')
        elif "wakes" in record:
            time_awake = re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}', record)
            time_awake = datetime.strptime(time_awake.group(), '%Y-%m-%d %H:%M')
            while time_asleep < time_awake:
                guards[guard_id].append(time_asleep.minute)
                time_asleep += timedelta(minutes=1)
            time_asleep = 0
    most_common = (0, 0)
    id_most_common = 0
    for guard_id in guards:
        guard_most_common = Counter(guards[guard_id]).most_common(1)[0]
        if guard_most_common[1] > most_common[1]:
            most_common = guard_most_common
            id_most_common = guard_id
    return id_most_common * most_common[0]


print(strategy_1(lines))
print(strategy_2(lines))
