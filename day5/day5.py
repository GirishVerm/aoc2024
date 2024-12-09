txt = open('day5/input.txt', 'r')

list_toggle = False
pair_dictionary = {}

num_lists = []
for line in txt:
    if line == '\n':
        list_toggle = True

    if list_toggle:
        if line != '\n':
            # process list
            temp_list = line.split(',')
            temp_list[-1] = temp_list[-1].strip()
            if len(temp_list) != 0:
                temp_list = [int(x) for x in temp_list]
                num_lists.append(temp_list)

    else: 
        # process pairs
        pair = line.split('|')
        pair_dictionary[int(pair[0])] = set([])
        pair_dictionary[int(pair[1].strip())] = set([])

txt2 = open('day5/input.txt', 'r')
list_toggle = False
for line in txt2:
    if line == '\n':
        list_toggle = True

    if not list_toggle: 
        # process pairs
        pair = line.split('|')
        pair_dictionary[int(pair[0])].add(int(pair[1].strip()))

valid_lists = []
invalid_lists = []
for num_list in num_lists:

    valid = True
    for index in range(len(num_list)):

        subset = set(num_list[index+1:])
        if subset.issubset(pair_dictionary[num_list[index]]):
            continue
        else:
            valid = False
            break
    if valid:
        valid_lists.append(num_list)
    else:
        invalid_lists.append(num_list)

for num_list in invalid_lists:

    for num in range(len(num_list)):
        valid = True
        for index in range(len(num_list)):
            subset = set(num_list[index+1:])
            if not subset.issubset(pair_dictionary[num_list[index]]):
                num_list[index+1], num_list[index] = num_list[index], num_list[index+1]

        for index in range(len(num_list)):

            subset = set(num_list[index+1:])
            if subset.issubset(pair_dictionary[num_list[index]]):
                continue
            else:
                valid = False
                break

        if valid:
            break
        else:
            continue


sum = 0
for num_list in invalid_lists:
    sum += num_list[len(num_list) // 2]
print(sum)