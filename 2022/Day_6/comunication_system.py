with open("input.txt", "r") as f:
	data = f.readline()


i= 0
# print(da)
while(True):
	unique_letters = data[i:(i+14)] # take it from 4 to 4 for part one and 14 to 14 for part 2
	if len(set(list(unique_letters))) == 14:
		print(i + 14)
		break
	i+=1