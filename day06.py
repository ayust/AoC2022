with open("day06.input.txt") as f:
    data = f.read().strip()
    for i in range(4, len(data)):
        window = set(data[i - 4 : i])
        if len(window) == 4:
            print(i)
            break
    for i in range(14, len(data)):
        window = set(data[i - 14 : i])
        if len(window) == 14:
            print(i)
            break
