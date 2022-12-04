with open("input.txt", "r") as f:
	data = [line.strip() for line in f.readlines()]

def is_fully_contained(a:str,b:str) -> int:
	rangeA = [int(i) for i in a.split('-')]
	rangeB = [int(i) for i in b.split('-')]

	if (rangeA[0] <= rangeB[0]) and (rangeA[1] >= rangeB[1]):
		return 1
	elif (rangeB[0] <= rangeA[0]) and (rangeB[1] >= rangeA[1]):
		return 1

	return 0

total = 0

for x in data:
	elf_1, elf_2 = x.split(',') # take the strings in variables
	total += is_fully_contained(elf_1,elf_2)
print(total) # 540

# My logic in the is_fully_contained function was:
# if the min(from value) value of the range is equal or less than the first one in the second range
# and the max(to value) is greater or equal than the second range then it was fully contained
# I spent like an hour and then I thought how I know just by looking at it that is fully contained?
# a few seconds looking for the conditions and then became clear, first try was correct
# the elif part check is the second group has those conditions example:
# [2, 8] [3, 7] is true for the if and for the elif [6, 6] [4, 6] this is true