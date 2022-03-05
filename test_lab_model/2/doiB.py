
def poz_max(lista):
    maxim = max(lista)
    i = 0
    ans = []
    for x in lista:
        i += 1
        if x == maxim:
            ans.append(i)

    return ans
