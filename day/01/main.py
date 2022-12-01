top1, top2, top3 = (sorted([sum(map(int, elf)) for elf in [line.split(
    "\n") for line in open('input.txt', 'r').read().split("\n\n")]], reverse=True)[:3])

print("Top 1:", top1)
print("Top 3:", sum([top1, top2, top3]))
