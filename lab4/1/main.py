
fo = open('test.out', 'w')
nota = 10

with open('test.in', 'r') as fi:
    for line in fi:
        termeni = [int(x) for x in line[:-1].replace("=", "*").split("*")]
        if termeni[0] * termeni[1] == termeni[2]:
            fo.write(line[:-1] + ' Corect\n')
        else:
            fo.write(line[:-1] + ' Gresit\n')
            nota -= 1
    fo.write(f"Nota {nota}\n")

