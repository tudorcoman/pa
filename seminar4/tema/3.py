
#a:

def numberOfElements(list, fn):
    ans = 0
    for element in list:
        ans += fn(element)
    return ans




#b:

from math import gcd

even = (lambda x: True if x % 2 == 0 else False)
testList = [i for i in range(100)]

print(numberOfElements(testList, even))


vocal = (lambda ch: True if ch in "aeiouAEIOU" else False)
testStr = "Ana are mere"

print(numberOfElements(testStr, vocal))

equalTuple = (lambda xy: True if xy[0] == xy[1] else False)
testArray = [(1, 1), (1, 2), (1, 3), (2, 2), (3, 3), (2, 4), (3, 4), (4, 3)]

print(numberOfElements(testArray, equalTuple))

kLength = (lambda k: (lambda x: True if len(x) == k else False))
strList = ["Ana", "are", "mere"]

print(numberOfElements(strList, kLength(3)))

filterCmmdc = (lambda y, t: (lambda x: True if gcd(x, y) == t else False))
testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(numberOfElements(testList, filterCmmdc(5, 5)))
