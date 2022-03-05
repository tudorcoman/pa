import re

sentence = "Ana are prune si gutui verzi, dar mai multe prune decat gutui!"
separators = [',', '.', '!', '?']

for sep in separators:
    sentence = sentence.replace(sep, " ")

words = sentence.split()
s = {}

for w in words:
    if w in s:
        s[w] += 1
    else:
        s[w] = 1

print([k for k in s.keys()])
