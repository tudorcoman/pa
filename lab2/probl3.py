
phrase = input().split()
s = input()
t = input()

new_phrase = ""
for word in phrase:
    new_word = word
    if word == s:
        new_word = t
    new_phrase += " " + new_word

new_phrase = new_phrase[1:]
print(new_phrase)
