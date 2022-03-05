
from doiA import modifica_prefix
from doiB import poz_max

a, b = input().split(" ")

maxUpdates = 0
sol = []
k = 0

with open("propozitii.in", "r") as input:
    output = open("propozitii_modificate.out", "w")
    for propozitie in input:
        k += 1
        new_line, updates = modifica_prefix(a, b, propozitie)
        output.write(new_line)
        if updates > maxUpdates:
            maxUpdates = updates
            sol = [k]
        elif updates == maxUpdates:
            sol.append(k)

    output.close()
    print(*sorted(sol))
        
