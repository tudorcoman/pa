
phrase = input()
numbers = [int(x) for x in phrase.split() if x.isnumeric()]

s = sum(numbers)
print(s, "RON")

print(sum([int(x) for x in input().split() if x.isnumeric()]), "RON")
