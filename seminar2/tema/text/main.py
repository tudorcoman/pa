from collections import OrderedDict
from functools import cmp_to_key

def make_key(string):
    return ''.join(OrderedDict.fromkeys(sorted(string.lower())).keys())

def punctuatie(ch):
    return ch in "!:;,.?"

def key_cmp(a, b):
    if len(a) > len(b):
        return -1
    elif len(a) == len(b):
        return 1 if a > b else -1
    else:
        return 1

dict = {}
str_cmp_key = cmp_to_key(key_cmp)

with open('exemplu.txt', 'r') as f:
    for line in f:
        parsed_line = line
        for p in "!:;,.?":
            parsed_line = parsed_line.replace(p, '')

        for word in parsed_line.split():
            key = make_key(word)
            if key in dict:
                dict[key].add(word.lower())
            else:
                dict[key] = set()
                dict[key].add(word.lower())

    keys = list(dict.keys())
    keys.sort(key=str_cmp_key)
    print(keys, dict.keys())
    for key in keys:
        print(f"Literele {key}:", *sorted(dict[key])) 
