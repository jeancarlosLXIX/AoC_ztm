with open("input.txt", "r") as f:
	data = [line.strip() for line in f.readlines()]

shape_to_use = {"X":1, "Y":2, "Z":3}

def shape_use(rival: str,condition:str)-> int:
	"""This function will take the rival choise and the the condicion, returning an int value
		based on the condition (second column of rh input.txt) and the rival choise"""
	win_lose_draw = ''
	if condition == 'Z':
		win_lose_draw = 'W'
	elif condition == 'X':
		win_lose_draw = 'L'
	else:
		win_lose_draw = 'D'
	
	match rival:
		
		case 'A': # ROCK
			if win_lose_draw == 'D':
				return shape_to_use['X']
			elif win_lose_draw == 'L':
				return shape_to_use['Z']
			elif win_lose_draw == 'W':
				return shape_to_use['Y']
		
		case 'B': # PAPER
			if win_lose_draw == 'D':
				return shape_to_use['Y']
			elif win_lose_draw == 'L':
				return shape_to_use['X']
			elif win_lose_draw == 'W':
				return shape_to_use['Z']

		case 'C': # SCISSORS
			if win_lose_draw == 'D':
				return shape_to_use['Z']
			elif win_lose_draw == 'L':
				return shape_to_use['Y']
			elif win_lose_draw == 'W':
				return shape_to_use['X']


def round2():
	total_score_updated = 0
	for i,row in enumerate(data):
		what_to_do = row[2]
		selected_value = shape_use(row[0], what_to_do)		
		
		if what_to_do == 'X':
			total_score_updated += selected_value
		elif what_to_do == 'Y':
			total_score_updated += selected_value + 3
		else:
			total_score_updated += selected_value + 6

	return total_score_updated

print(round2())
# 12627 wrong
# 12779 wrong
# 12767 right