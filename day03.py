from string import ascii_letters

priorities = {y: x + 1 for x, y in enumerate(ascii_letters)}

with open("day03.input.txt") as f:
    lines = [l.rstrip() for l in f]
    total = 0
    for line in lines:
        first, second = line[: len(line) // 2], line[len(line) // 2 :]
        shared = set(first) & set(second)
        total += priorities[list(shared)[0]]
    print(total)

    total = 0
    for i in range(0, len(lines), 3):
        first, second, third = lines[i : i + 3]
        shared = set(first) & set(second) & set(third)
        total += priorities[list(shared)[0]]
    print(total)
