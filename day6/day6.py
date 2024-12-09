txt = open('day6/input.txt', 'r')
lab = []
for line in txt:
    lab.append(list(line.strip()))

vert = len(lab)
horz = len(lab[0])

row = 0
col = 0

for _row in range(len(lab)):
    for _col in range(len(lab[_row])):
        if lab[_row][_col] == "^":
            row = _row
            col = _col
            break
sign = lab[row][col]

def getBreakCondition(row, col, sign):
    if row == len(lab) - 1 and sign == "v":
        return False
    if row == 0 and sign == "^":
        return False
    if col == len(lab[0]) - 1 and sign == ">":
        return False
    if col == 0 and sign == "<":
        return False
    else:
        return True

sum = 0

while getBreakCondition(row, col, sign):
    
    if sign == "^": # Facing upwards

        # Check for obstacle 
        if lab[row-1][col] == "#":
            sign = ">" # turn right 90 degrees
        else:
            if lab[row][col] != "X":
                sum += 1
            lab[row][col] = "X"
            row = row - 1 # Move up
            col = col 
            
    if sign == ">": # Facing upwards

        # Check for obstacle 
        if lab[row][col+1] == "#":
            sign = "v" # turn right 90 degrees
        else:
            if lab[row][col] != "X":
                sum += 1
            lab[row][col] = "X"
            row = row 
            col = col + 1 # Move right
    
    if sign == "v": # Facing upwards

        # Check for obstacle 
        if lab[row+1][col] == "#":
            sign = "<" # turn right 90 degrees
        else:
            if lab[row][col] != "X":
                sum += 1
            lab[row][col] = "X"
            row = row + 1 # Move down
            col = col 
    
    if sign == "<": # Facing upwards

        # Check for obstacle 
        if lab[row][col - 1] == "#":
            sign = "^" # turn right 90 degrees
        else:
            if lab[row][col] != "X":
                sum += 1
            lab[row][col] = "X"
            row = row
            col = col - 1 # Move left

if lab[row][col] != "X":
    sum += 1
    lab[row][col] = "X"

for row in lab:
    print(row)
print(sum)
