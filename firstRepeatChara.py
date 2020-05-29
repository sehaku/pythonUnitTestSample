def findRucurringChara(str):
    list = []
    for char in str:
        if char in list:
            return char
        else:
            list.append(char)
    return None
    """
    line = []
    for i in range(len(str)):
        compare = str[i:i+1]
        if (line.count(compare) != 0):
            return compare
        else:
            line.append(compare)
    return None
    """


print(findRucurringChara("testCase"))
