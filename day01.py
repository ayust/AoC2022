with open("day01.input.txt") as f:
    lines = [l.rstrip() for l in f]
    subtotals = []
    subtotal = 0
    for line in lines:
        if not line:
            subtotals.append(subtotal)
            subtotal = 0
            continue
        subtotal += int(line)
    if subtotal:
        subtotals.append(subtotal)
    subtotals.sort()
    print(subtotals[-1], sum(subtotals[-3:]))
