
with open("inventar.txt", "r") as f:
    dicti = {}
    for line in f:
        tok = line.split(" ")
        name = tok[0]

        setul = set()
        for token in tok:
            if token != name:
                setul.add(int(token))

        dicti[name] = setul

    
    inters = set()
    reun = set()

    started = 0

    for key in dicti.keys():
        reun = reun.union(dicti[key])
        if not started:
            inters = dicti[key]
            started = 1
        else:
            inters = inters.intersection(dicti[key])

    print(*inters)
    print(*reun)




    for magazin in dicti.keys():
        dif = dicti[magazin]
        for key in dicti.keys():
            if key != magazin:
                dif = dif - dicti[key]
        
        print(magazin, end=" ")
        print(*sorted(dif))
        
