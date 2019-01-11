import random

#generate random numbers
def randomNumbers():
    randomNumList = []
    while len(randomNumList) < 10:
        num = random.randint(-100, 100)
        if num not in randomNumList:
            randomNumList.append(num)
    
    randomNumList.sort()
    #print(randomNumList)
    return randomNumList

#positive.py
def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return result

#negative.py
def negative(l):
    result = []
    for i in l:
        if i < 0:
            result.append(i)
    return result

#print all result
randomNumerResult = randomNumbers()
print(randomNumerResult)
print("그 중 양수는 : ", positive(randomNumerResult))
print("그 중 음수는 : ", negative(randomNumerResult))
if 0 in randomNumerResult:
    print("Zero가 존재합니다!!")
