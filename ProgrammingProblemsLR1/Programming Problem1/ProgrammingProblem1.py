import statistics

def median(numList):
    numList.sort()
    x = len(numList)
    med = int(x / 2);
    if(x % 2 == 1):
        return numList[med]
    else:
        return (numList[med] + numList[med + 1]) / 2

def mode(numList):
    mod = max(set(numList), key = numList.count)
    return mod
    
def mean(numList):
    x = len(numList)
    sumList = 0
    for i in numList:
        sumList = sumList + i;
    return sumList / x

numList = [27, 48, 49, 16, 3, 11, 19, 13, 29, 50]
print(median(numList))
print(mode(numList))
print(mean(numList))
