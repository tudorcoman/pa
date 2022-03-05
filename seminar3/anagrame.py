def anagrame1(a, b):
    if len(a) != len(b):
        return False
    else:
        bb = list(b)
        for i in range(len(a)):
            if a[i] in bb:
                pos = 0
                found = False
                while pos < len(bb) and not found:
                    if bb[pos] == a[i]:
                        found = True
                    else:
                        pos += 1
                bb[pos] = ' '
            else:
                return False
        else:
            return True

def get_freq(a):
    f = {}
    for ch in a:
        try:
            f[ch] += 1
        except KeyError:
            f[ch] = 1
    return f

def anagrame2(a, b):
    return get_freq(a) == get_freq(b)

def anagrame3(a, b):
    return sorted(a) == sorted(b)


def afisare(flag):
    print("anagrame" if flag else "nu sunt anagrame")

a = input()
b = input()

afisare(anagrame1(a, b))
afisare(anagrame2(a, b))
afisare(anagrame3(a, b))    
