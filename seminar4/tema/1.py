def generateLists(x, *lists):
    for list in lists:
        if x in list:
            yield list
