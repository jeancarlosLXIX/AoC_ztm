import re
with open("input.txt", "r") as f:
	instructions = [line.strip() for line in f.readlines()]

def print_lastest():
        for i in crates.keys():
            if len(crates[i]) > 0:
                print(crates[i][-1],end="")

def move_crane(amount: int, from_:int, to:int):
            taken_values = crates[from_][-amount:] # if [1,2,3] [-2:] returns [2,3]
            while(len(taken_values)): # once the length 0is 0 it finishes
                    crates[to].append(taken_values.pop(0)) # if [2,3] after the first pop(0) list is [3]
            crates[from_] = crates[from_][:-amount] # if [1,2,3] [:-2] returns [1]

crates = {
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

for instruction in instructions:
		matches = [int(val) for val in re.findall("[0-9]", instruction)]
		if len(matches) > 3: # is the numers has 2 digists it will return in separe, example 10 becomes [1,0]
			fixed = int(str(matches[0])+str(matches[1]))
			move_crane(fixed,matches[2],matches[3])
		else:
			move_crane(matches[0],matches[1],matches[2])
print_lastest() # VRQWPDSGP