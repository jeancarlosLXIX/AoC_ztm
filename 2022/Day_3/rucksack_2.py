from rucksack import fill_items

with open("input.txt", "r") as f:
	data = [line.strip() for line in f.readlines()] # strip to remove \n

def common_item(a:str,b:str,c:str):
    for x in a:
        if x in b: # if x = r it will check if the other 2 has r in it
            if x in c:
                return x

item_types = fill_items()
total = 0

# https://stackoverflow.com/questions/28562966/loop-in-python-list-using-more-than-one-item-per-loop 
for a, b, c in zip(*[iter(data)]*3):
    total += item_types[common_item(a,b,c)]

print(total) # 2817