
def multiplicationTable(n):
    return [[i * j for j in range(1, n + 1)] for i in range(n)]

n = int(input())
print(multiplicationTable(n))
