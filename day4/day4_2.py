txt = open('day4/input.txt', 'r')
big_array = []

for line in txt:
    big_array.append(list(line.strip()))

X_list = []
sum = 0
sumA = 0
ref_set = set(["A", "M", "S"])
for row in range(len(big_array)):
    for col in range(len(big_array[row])):
        if big_array[row][col] == "A":
            sumA += 1
            # Criss
            if (row - 1 >= 0 and row + 1 < len(big_array)) and (col + 1 < len(big_array[row]) and col - 1 >= 0):
                criss = set([
                    big_array[row - 1][col - 1], #Left Up
                    big_array[row][col],
                    big_array[row + 1][col+1], #Right Down
                    ])

                cross = set([
                    big_array[row + 1][col - 1], #Left Down
                    big_array[row][col],
                    big_array[row-1][col+1], #Right Up
                    ])
                if criss == ref_set and cross == ref_set:
                    print("MAS Center at", "[%d][%d]" % (row, col))
                    sum += 1
                
print(sumA)
print(sum)


            