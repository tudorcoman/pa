import re

REPEATER = re.compile(r"(.+?)\1+$")

def repeated(s):
    match = REPEATER.match(s)
    return match.group(1) if match else None

s = input()
sub = repeated(s)

if sub:
    x = len(s)//len(sub)
    print(x, s[:len(sub)])
else:
    print("Imposibil")
