
def cautare(L, x, st, dr):
    if st > dr:
        return False

    mid = (st + dr) // 2
    if x == L[mid]:
        return True

    if x < L[mid]:
        return cautare(L, x, st, mid - 1)

    return cautare(L, x, mid + 1, dr)


L = [2, 5, 7, 8, 10, 12, 15, 17, 25]
S = 20
N = len(L)

for elem in L:
    target = S - elem
    if cautare(L, target, 0, N - 1) and elem < target:
        print(min(elem, target), max(elem, target))

