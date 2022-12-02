with open("input.txt", "r") as f:
	data = [line for line in f.readlines()]

#? X for Rock, Y for Paper, and Z for Scissors. this is me
#! A for Rock, B for Paper, and C for Scissors this is the opponent
#* outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

shape_to_use = {"X":1, "Y":2, "Z":3}
total_score = 0

def round(rival:str, me: str)-> str:
	"""The is for the first part, returns a letter to let doy know if you:
		D = draw 
		W = win
		L = lose"""
	if (rival == 'A' and me=='X') or (rival == 'B' and me=='Y') or (rival == 'C' and me=='Z'):
		return 'D' 
	elif (rival == 'A' and me == 'Y') or (rival == 'B' and me == 'Z') or (rival == 'C' and me == 'X'):
		return 'W'
	else:
		return 'L'

for row in data:
	me_a_chad = row[2]
	selected_shape_point = shape_to_use[me_a_chad]

	result = round(row[0],me_a_chad)
	
	if result == 'D':
		total_score += (selected_shape_point + 3)
	elif result == 'W':
		total_score  += (selected_shape_point + 6)
	else:
		total_score += selected_shape_point

print(f"Total score part 1: {total_score}")