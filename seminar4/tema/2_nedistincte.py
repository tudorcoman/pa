L = [2, 5, 5, 5, 7, 8, 10, 10, 12, 15, 15, 17, 25]
S = 20
dicti = {}

for elem in L:
    try:
        dicti[elem] += 1
    except KeyError:
        dicti[elem] = 1

pairs = 0
for key in dicti.keys():
    try:
        if key < S and key != (S // 2) and dicti[key] > 0 and dicti[S - key] > 0:
            pairs += dicti[key] * dicti[S - key]
    except KeyError:
        pass

pairs = pairs // 2
try:
    if S % 2 == 0 and dicti[S // 2] > 1:
        ap = dicti[S // 2]
        cmb = ap * (ap - 1) // 2
        pairs += cmb
except KeyError:
    pass


print(pairs)
