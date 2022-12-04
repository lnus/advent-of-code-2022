lines = [line.strip() for line in open('input.txt')]

# Part 1
ans = 0

for line in lines:
    c1, c2 = line[:len(line)//2], line[len(line)//2:]

    # Finds the character that appears in both strings
    unique = (set(c1) & set(c2)).pop()

    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    if unique.islower():
        ans += ord(unique) - 96
    elif unique.isupper():
        ans += ord(unique) - 38

print(ans)

# Part 2
ans = 0

# splits into groups of 3
chunks = [lines[i:i+3] for i in range(0, len(lines), 3)]

for chunk in chunks:
    x, y, z = chunk
    common = (set(x) & set(y) & set(z)).pop()  # group id

    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    if common.islower():
        ans += ord(common) - 96
    elif common.isupper():
        ans += ord(common) - 38

print(ans)
