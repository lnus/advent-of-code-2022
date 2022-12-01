topwhatever = 3
print(sum(sorted([sum(map(int, elf)) for elf in [list(filter(None, line.split("\n")))
      for line in open('input.txt', 'r').read().split("\n\n")]], reverse=True)[:topwhatever]))
