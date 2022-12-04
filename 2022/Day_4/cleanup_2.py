with open("input.txt", "r") as f:
	data = [line.strip() for line in f.readlines()]

total = 0
for line in data:
    elves = line.split(",")
    ranges = [list(map(int, elf.split("-"))) for elf in elves]

    a, b = ranges[0]
    c, d = ranges[1]

    if not (b < c or a > d):
        total += 1

print(total) # 872
# 935 too high
# 351 too low
# 568 wrong
# 589 wrong
# 588 wrong
# 532 wrong
# 204 wrong