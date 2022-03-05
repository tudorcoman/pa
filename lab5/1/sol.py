import random


# a
# ------------------------
def generare_timpi():
    with open("tis.txt", "w") as file_output:
        nr_persoane = random.randint(5, 15)
        #file_output.write(f"{nr_persoane}\n")
        times = [x for x in range(1, 21)]
        waiting_times = random.choices(times, k=nr_persoane)
        for x in waiting_times:
            file_output.write(f"{x}\n")


# b
# ------------------------
def citire():
    with open("tis.txt", "r") as file_input:
        input_lines = file_input.readlines()
        nr_persoane = len(input_lines)
        lista = []
        for i in range(nr_persoane):
            lista.append((i, int(input_lines[i])))
        return lista

# c
# ------------------------
def afisare_timpi_servire(lista):
    timp = 0
    timp_total = 0
    for x in lista:
        timp += x[1]
        print(f"{x[0]} {x[1]} {timp}")
        timp_total += timp
    timp_mediu = timp_total / len(lista)
    print(timp_mediu)

# d
# ------------------------
def rez_greedy(lista):
    lista.sort(key=lambda x: x[1])

# Executare cod
# ------------------------
generare_timpi()
lista_persoane = citire()
afisare_timpi_servire(lista_persoane)
rez_greedy(lista_persoane)
afisare_timpi_servire(lista_persoane)
