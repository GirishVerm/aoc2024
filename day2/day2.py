import math

file1 = open('day2/input.txt', 'r')
sum = 0

def strToInt(strList):

    return [int(text) for text in strList]

def isSafe(numList):

    toggle = True
    inc = False
    dec = False

    for index in range(len(numList)-1):
        difference = math.fabs(numList[index] - numList[index+1])
        
        if not (difference <= 3 and difference >=1):
            toggle = False
         
        if numList[index] < numList[index+1]:
            inc = True
          
        elif numList[index] > numList[index+1]:
            dec = True  
    
    # if toggle and not (inc == dec):
    #     print("safe", numList, sep=' ')
    # else:
    #     print("unsafe", numList, sep=' ')
    return toggle and not (inc == dec)
            
def breaker(numList):
    resultList = []

    for index in range(len(numList)):
        tempList = numList[:]
        tempList.pop(index)
        resultList.append(tempList)
    
    return resultList


for line in file1:
    numList = strToInt(line.split())
    for version in breaker(numList):
        
        # break lists into variations, if one version found safe, break
        if isSafe(version):
            print(numList, version)
            sum += 1
            break

print(sum)