import math 

file1 = open('day1/input.txt', 'r')
list1 = []
list2 = []

list2_dict = {}

# {
#     num: 0
# }

for numbers in file1:
    numbers_list = numbers.split()
    num1 = int(numbers_list[0])
    num2 = int(numbers_list[-1])

    list2_dict[num1] = 0
    list2_dict[num2] = 0

    list1.append(num1)
    list2.append(num2)

# list1 = sorted(list1)
# list2 = sorted(list2)

sum = 0

for number in list2:
    list2_dict[number] += 1



for index in range(len(list1)):
    sum += list1[index] * list2_dict[list1[index]]


   
print(sum)
