
with open("inputs.txt", "r") as f:
    data = f.readlines()


most_calories = 0
current = 0


for x in data:
    if x == "\n":
        if current > most_calories:
            most_calories = current
            current = 0
        else:
            current = 0
        
    else:
        current += int(x)

print("Elf with most calories: ", most_calories)