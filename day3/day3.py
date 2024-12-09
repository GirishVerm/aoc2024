regexOne = "[m]{1}[u]{1}[l]{1}[(]{1}\d{1,3}[,]\d{1,3}[)]{1}"
regex = "[m]{1}[u]{1}[l]{1}[(]{1}\d{1,3}[,]\d{1,3}[)]{1}|[d]{1}[o]{1}[(]{1}[)]{1}|[d]{1}[o]{1}[n]{1}[']{1}[t]{1}[(]{1}[)]{1}"
regexDo = "[d]{1}[o]{1}[(]{1}[)]{1}"
regexDont = "[d]{1}[o]{1}[n]{1}[']{1}[t]{1}[(]{1}[)]{1}"
regex2 = "\d{1,3}[,]\d{1,3}"


import re

txt = open('day3/input.txt', 'r')
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":

x = re.findall(regexOne, txt.read())

toggle = True
z = []
for string in x:
    if string == "don't()":
        print(string)
        print("disabled")
        toggle = False
    if string == "do()":
        print(string)
        print("enabled")
        toggle = True
    if(toggle):
        if string != "do()":
            print("valid", string)
            z.append(string)
    else:
        print("ignorning", string)

y = re.findall(regex2, ''.join(x))


sum = 0
for string in y:
    pair = string.split(',')
    sum += int(pair[0]) * int(pair[1])

print(sum)
