# O(C + NlogN), unde C = nr caractere din text si N = numarul maxim de cuvinte cu acelasi numar de litere

d = {}

with open("exemplu.txt", "r") as f:
    maxLen = 0
    for line in f:
        words = line.split()
        for word in words:
            word = "".join([c for c in word if c.isalpha()])
            if len(word) > maxLen:
                maxLen = len(word)
            try:
                d[len(word)].append(word)
            except KeyError:
                d[len(word)] = [word]

    for len in range(maxLen, 0, -1):
        if len in d:
            print(f"Lungimea {len}: " + str(sorted(set(d[len]))))
    
