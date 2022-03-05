
a = input()
b = input()

if len(a) != len(b):
    print("nu sunt anagrame")
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
            print("nu sunt anagrame")
            break
    else:
        print("anagrame") 
