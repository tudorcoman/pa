
def filterLists(x, *lists):
    sol = []
    for list in lists:
        if x in list:
            sol.append(list)
    return sol


def generateLists(x, *lists):
    for list in lists:
        if x in list:
            yield list

l1 = [1, 2, 3]
l2 = [4, 5]
l3 = [1, 2, 3, 6, 7]
l4 = [1, 2]

print(filterLists(3, l1, l2, l3, l4))
