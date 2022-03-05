
def get_freq(a):
    f = {}
    for ch in a:
        try:
            f[ch] += 1
        except KeyError:
            f[ch] = 1
    return f

a = input()
b = input()
print("anagrame" if get_freq(a) == get_freq(b) else "nu sunt anagrame") 
