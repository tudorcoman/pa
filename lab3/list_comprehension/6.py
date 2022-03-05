
def sameParity(lista):
    return [lista[i] for i in range(len(lista)) if i % 2 == lista[i] % 2]

print(sameParity([2, 4, 1, 7, 5, 1, 8, 10]))
