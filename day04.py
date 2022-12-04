with open("day04.input.txt") as f:
    lines = [l.rstrip() for l in f]
    total = 0
    for line in lines:
        first, second = line.split(",")
        a, b = first.split("-")
        c, d = second.split("-")
        a, b, c, d = int(a), int(b), int(c), int(d)
        if (c <= a and b <= d) or (a <= c and d <= b):
            total += 1
    print(total)

    total = 0
    for line in lines:
        first, second = line.split(",")
        a, b = first.split("-")
        c, d = second.split("-")
        a, b, c, d = int(a), int(b), int(c), int(d)
        if (c <= a <= d) or (c <= b <= d) or (a <= c <= b) or (a <= d <= b):
            total += 1
    print(total)
