def largetElement(list):
    maxIndex:int = 0
    for i in range(len(list)):
        if list[maxIndex] < list[i]:
            maxIndex = i
    return list[maxIndex]

