
def modifica_prefix(x, y, prop):
    lungimePrefix = len(x)
    words = [y + word[lungimePrefix:] if word[:lungimePrefix] == x else word for word in prop.split(" ")]
    nr = 0
    for word in prop.split(" "):
        if word[:lungimePrefix] == x:
            nr += 1

    propozitie = " ".join(words)
    return propozitie, nr
