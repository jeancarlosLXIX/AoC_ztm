import re
with open("input.txt", "r") as f:
	instructions = [line.strip() for line in f.readlines()]

crates = { # UGLY HARD CODE I KNOW IT JIMMY!!!
	1:list("NBDTVGZJ"),
	2:list("SRMDWPF"),
	3:list("VCRSZ"),
	4:list("RTJZPHG"),
	5:list("TCJNDZQF"),
	6:list("NVPWGSFM"),
	7:list("GCVBPQ"),
	8:list("ZBPN"),
	9:list("WPJ")
}

def print_lastest():
	for i in crates.keys():
		if len(crates[i]) > 0:
			print(crates[i][-1],end="")

def move_crane(amount: int, from_:int, to:int):
		for i in range(amount):
			if len(crates[from_]) > 0:
				taken_value = crates[from_].pop()
				crates[to].append(taken_value)
			else:
				return
if __name__ == "__main__":
	for instruction in instructions:
		matches = [int(val) for val in re.findall("[0-9]", instruction)]
		if len(matches) > 3:
			fixed = int(str(matches[0])+str(matches[1]))
			move_crane(fixed,matches[2],matches[3])
		else:
			move_crane(matches[0],matches[1],matches[2])
	print_lastest() # GFTNRBZPF