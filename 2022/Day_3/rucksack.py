with open("input.txt", "r") as f:
	data = [line.strip() for line in f.readlines()] # strip to remove \n


def fill_items(): # O(n)
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = lower_case.upper()
	obj = {}
	
	# a through z have priorities 1 through 26.
	for i,x in enumerate(lower_case):
		obj[x] = i + 1

	# A through Z have priorities 27 through 52.
	for i,x in enumerate(upper_case): # since i start at 0 we add up 1
		obj[x] = i + obj["z"] + 1
	
	return obj

def common_letter(a:str, b:str): # O(n)
	values = {}
	total_for_this =0
	for j in a:
		if j in b:
			values[j] = 1
	
	if  bool(values):
		for key in values.keys():
			total_for_this += (item_types[key] * values[key])
	
	return total_for_this
	


if __name__ == "__main__": # since I am importing the fill_items function this will prevent this code from running every time
	item_types = fill_items()
	total = 0
	for x in data: # O(n^2)
		middle = round(len(x)/2)
		first_part = x[:middle]
		second_part = x[middle:]
		total += common_etter(first_part,second_part) # n + 1

	print(total) # 8185 right
