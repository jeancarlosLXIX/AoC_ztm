with open("inputs.txt", "r") as f:
    data = f.readlines()

top_three = {1:0,2:0,3:0}
current = 0

def sum_all(obj: dict) -> int:
    """Sum all the values of our object to return them as int"""
    total = 0
    for x in obj.values():
        total += x
    
    return total


# Why append a line at the end?
# I was geting bad result because at the last number of the test file (ends up in 10,000)
# I did not understood why but while I was printing  I notice that it did not print the current sum (the last one)
# so adding an extra element being a new line allows us to properly  check the last value (10,000) 
data.append("\n")

for x in data:
   
   if x == "\n":
    if current > top_three[1]:
        top_three[3] = top_three[2]
        top_three[2] = top_three[1]
        top_three[1] = current

    elif current > top_three[2]:
        top_three[3] = top_three[2]
        top_three[2] = current
        
    elif current > top_three[3]:
        top_three[3] = current
        
    current = 0
   else:
        current += int(x)

print(sum_all(top_three))