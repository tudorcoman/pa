
def punctuatie(ch):
    return ch in "!:;,.?"

string = input()

print(f"Litere mici: ", sum(1 for c in string if c.islower()))
print(f"Litere mari: ", sum(1 for c in string if c.isupper()))
print(f"Semne de punctuatie: ", sum(1 for c in string if punctuatie(c)))
