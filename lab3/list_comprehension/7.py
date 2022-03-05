
def makePairs(lista):
    return [(lista[i], lista[i + 1]) for i in range(len(lista) - 1)]

print(makePairs([1, 2, 3, 4]))
