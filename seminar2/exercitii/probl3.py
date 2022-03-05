import re

words = [w for w in re.split("(\W+)", input()) if w.isalnum()] 
s = set()

lmax = 0
for w in words:
    if len(w) > lmax:
        lmax = len(w)
        s = set([w])
    elif len(w) == lmax:
        s.add(w)

print(s)
