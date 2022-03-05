

with open("cuburi.txt", "r") as f:
    lines = f.readlines()
    N = int(lines[0])


    lista = []

    for i in range(1, N+1):
        tok = lines[i].split(" ")
        lat = int(tok[0])
        culoare = tok[1][:-1]
        lista.append((lat, culoare))

    lista_sortata = sorted(lista, key= lambda x: -x[0])

    
    last = (-1, "")
    out = open("turn.txt", "w")
    sum = 0

    for element in lista_sortata:
        if last[0] == -1 or (element[0] < last[0] and element[1] != last[1]):
            out.write("%d %s\n" % (element[0], element[1]))
            last = element
            sum += last[0]

    out.write("Inaltime totala: %d\n" % sum)
    out.close()
