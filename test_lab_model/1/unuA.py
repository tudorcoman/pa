
def citire_matrice(filename):
    m = []
    nr_elem = None
    with open(filename, "r") as input:
       for line in input:
           linie = [int(x) for x in line.split(" ")]
           if nr_elem == None:
               nr_elem = len(linie)
           elif len(linie) != nr_elem:
               return None
           m.append(linie)
    return m


#print(citire_matrice("matrice.in"))
