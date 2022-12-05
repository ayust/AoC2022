import re
from collections import defaultdict

with open("day05.input.txt") as f:
    lines = [l.rstrip("\n") for l in f]

    stacklines, movelines = lines[:8], lines[10:]

    stacks = defaultdict(list)
    for line in stacklines:
        s = 0
        for i in range(1, 4 * 9, 4):
            c = line[i]
            s += 1
            if c != " ":
                stacks[s].insert(0, c)

    for move in movelines:
        m = re.match("move (\d+) from (\d+) to (\d+)", move)
        count, start, end = int(m.group(1)), int(m.group(2)), int(m.group(3))
        for i in range(count):
            stacks[end].append(stacks[start].pop())

    result = "".join(stacks[i][-1] for i in range(1, 10))
    print(result)

    stacks = defaultdict(list)
    for line in stacklines:
        s = 0
        for i in range(1, 4 * 9, 4):
            c = line[i]
            s += 1
            if c != " ":
                stacks[s].insert(0, c)

    for move in movelines:
        m = re.match("move (\d+) from (\d+) to (\d+)", move)
        count, start, end = int(m.group(1)), int(m.group(2)), int(m.group(3))
        moved = stacks[start][-count:]
        stacks[end].extend(moved)
        stacks[start][-count:] = []

    result = "".join(stacks[i][-1] for i in range(1, 10))
    print(result)
