def areaStrToList(arStr):
    lst = [0,0,0,0]
    if (len(arStr) > 1):
        lst = list(map(lambda i: int(i),arStr[1:-1].split(",")))
        if (len(lst) != 4):
            lst = [0,0,0,0]
    return lst
