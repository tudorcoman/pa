propozitie = input()
dicti = {}

for word in propozitie.split(' '):
    mini = maxi = word
    try:
        dicti[word] += 1
    except KeyError:
        dicti[word] = 1


for key in dicti.keys():
    if dicti[key] < dicti[mini]:
        mini = key
    elif dicti[key] == dicti[mini] and key < mini:
        mini = key

    if dicti[key] > dicti[maxi]:
        maxi = key
    elif dicti[key] == dicti[maxi] and key < maxi:
        maxi = key


print(mini, maxi)
