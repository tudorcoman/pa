
words = input().split()

str = ""
for word in words:
    str += " " + word.capitalize()

str = str[1:]
print(str) 
