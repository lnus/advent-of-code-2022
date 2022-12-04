lines = [line.strip() for line in open('input.txt')]

total = 0

# Part 1
scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

# A and X are rock
# B and Y are paper
# C and Z are scissors

outcomes = {
    ('A', 'Y'): 6,  # Win
    ('A', 'X'): 3,  # Draw
    ('A', 'Z'): 0,  # Lose

    ('B', 'Z'): 6,  # Win
    ('B', 'Y'): 3,  # Draw
    ('B', 'X'): 0,  # Lose

    ('C', 'X'): 6,  # Win
    ('C', 'Z'): 3,  # Draw
    ('C', 'Y'): 0,  # Lose
}

for line in lines:
    opponent, me = line.split(" ")
    total += scores[me]
    total += outcomes[(opponent, me)]

print(total)

# Part 2
total = 0

# A - rock
# B - paper
# C - scissors
# (1 for Rock, 2 for Paper, and 3 for Scissors)

outcomes = {
    ('A', 'X'): 3,  # Lose vs rock (0 + 3, scissors)
    ('A', 'Y'): 4,  # Draw vs rock (3 + 1, rock)
    ('A', 'Z'): 8,  # Win vs rock (6 + 2, paper)

    ('B', 'X'): 1,  # Lose vs paper (0 + 1, rock)
    ('B', 'Y'): 5,  # Draw vs paper (3 + 2, paper)
    ('B', 'Z'): 9,  # Win vs paper (6 + 3, scissors)

    ('C', 'X'): 2,  # Lose vs scissors (0 + 2, paper)
    ('C', 'Y'): 6,  # Draw vs scissors (3 + 3, scissors)
    ('C', 'Z'): 7,  # Win vs scissors (6 + 1, rock)
}


for line in lines:
    opponent, me = line.split(" ")
    total += outcomes[(opponent, me)]

print(total)
