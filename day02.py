shape_scores = {"X": 1, "Y": 2, "Z": 3}
outcomes = {
    "A": {"X": 3, "Y": 6, "Z": 0},
    "B": {"X": 0, "Y": 3, "Z": 6},
    "C": {"X": 6, "Y": 0, "Z": 3},
}
inverse_outcomes = {
    "A": {"X": "Z", "Y": "X", "Z": "Y"},
    "B": {"X": "X", "Y": "Y", "Z": "Z"},
    "C": {"X": "Y", "Y": "Z", "Z": "X"},
}

with open("day02.input.txt") as f:
    lines = [l.rstrip() for l in f]
    total_score = 0
    for line in lines:
        abc, _, xyz = line.partition(" ")
        score = outcomes[abc][xyz] + shape_scores[xyz]
        total_score += score
    print(total_score)
    total_score = 0
    for line in lines:
        abc, _, xyz = line.partition(" ")
        xyz = inverse_outcomes[abc][xyz]
        score = outcomes[abc][xyz] + shape_scores[xyz]
        total_score += score
    print(total_score)
