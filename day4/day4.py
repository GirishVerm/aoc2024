txt = open('day4/input.txt', 'r')
big_array = []

for line in txt:
    big_array.append(list(line.strip()))

X_list = []
sum = 0
for row in range(len(big_array)):
    for col in range(len(big_array[row])):
        if big_array[row][col] == "X":

            # Right
            if col + 3 < len(big_array[row]):
                if big_array[row][col] + big_array[row][col+1] + big_array[row][col+2]+ big_array[row][col+3] == "XMAS" and (row,col):# not in X_list:
                    #X_list.append((row,col))
                    print("XMAS RIGHT at", "[%d][%d]" % (row, col))
                    sum += 1
            # Left
            if col - 3 >= 0:
                if big_array[row][col] + big_array[row][col-1] + big_array[row][col-2]+ big_array[row][col-3] == "XMAS" and (row,col):# not in X_list:
                    #X_list.append((row,col))
                    print("XMAS LEFT at", "[%d][%d]" % (row, col))
                    sum += 1

            # Up
            if row - 3 >= 0:
                if big_array[row][col] + big_array[row - 1][col] + big_array[row - 2][col]+ big_array[row - 3][col] == "XMAS" and (row,col):# not in X_list:
                    #X_list.append((row,col))
                    print("XMAS UP at", "[%d][%d]" % (row, col))
                    sum += 1

            # Down
            if row + 3 < len(big_array):
                if big_array[row][col] + big_array[row + 1][col] + big_array[row + 2][col]+ big_array[row + 3][col] == "XMAS" and (row,col):# not in X_list:
                    #X_list.append((row,col))
                    print("XMAS DOWN at", "[%d][%d]" % (row, col))
                    sum += 1

            # Next Implementation
            # Right Up
            if col + 3 < len(big_array[row]) and row - 3 >= 0:
                if big_array[row][col] + big_array[row - 1][col+1] + big_array[row - 2][col+2]+ big_array[row - 3][col+3] == "XMAS" and (row,col):# not in X_list:
                    #X_list.append((row,col))
                    print("XMAS RIGHT UP at", "[%d][%d]" % (row, col))
                    sum += 1


            # Left Up
            if col - 3 >= 0 and row - 3 >= 0:
                if big_array[row][col] + big_array[row - 1][col-1] + big_array[row - 2][col-2]+ big_array[row - 3][col-3] == "XMAS" and (row,col):# not in X_list:
                    #X_list.append((row,col))
                    print("XMAS LEFT UP at", "[%d][%d]" % (row, col))
                    sum += 1

            # Right Down
            if col + 3 < len(big_array[row]) and row + 3 < len(big_array):
                if big_array[row][col] + big_array[row + 1][col+1] + big_array[row + 2][col+2]+ big_array[row + 3][col+3] == "XMAS" and (row,col):# not in X_list:
                    #X_list.append((row,col))
                    print("XMAS RIGHT DOWN at", "[%d][%d]" % (row, col))
                    sum += 1

            # Left Down
            if col - 3 >= 0 and row + 3 < len(big_array):
                if big_array[row][col] + big_array[row + 1][col-1] + big_array[row + 2][col-2]+ big_array[row + 3][col-3] == "XMAS" and (row,col):# not in X_list:
                    #X_list.append((row,col))
                    print("XMAS LEFT DOWN at", "[%d][%d]" % (row, col))
                    sum += 1

print(sum)


            