def ek(ch, k):
    return chr(((ord(ch) - ord('a')) + k + 26) % 26 + ord('a')) if ch.isalpha() else ch

def dk(ch, k):
    return chr(((ord(ch) - ord('a')) - k + 26) % 26 + ord('a')) if ch.isalpha() else ch

op = input() # "encrypt" sau "decrypt"
k = int(input()) # k pentru cifrul lui Cezar
mesaj = input() # mesajul pe care facem encrypt/decrypt

if op == "encrypt":
    mesaj_nou = [ek(x, k) for x in mesaj]
else:
    mesaj_nou = [dk(x, k) for x in mesaj]

mesaj_nou = "".join([str(a) for a in mesaj_nou])
print(mesaj_nou)
