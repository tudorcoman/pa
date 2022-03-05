
from math import log2, sqrt

def f(x):
    return sqrt(x) * log2(x) + 4 * sqrt(x) + x * log2(x) - 793624157643927666

pow = 1
while f(pow) < 0:
    pow = pow * 2

sol = 0
while pow:
    if f(sol + pow) < 0:
        sol += pow
    pow /= 2

print(sol+1)
