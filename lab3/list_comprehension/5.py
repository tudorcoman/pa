
def keepOddPositions(lista):
    return [lista[i] for i in range(1, len(lista) + 1, 2)]

print(keepOddPositions([1, 2, 3, 4, 5, 6]))
