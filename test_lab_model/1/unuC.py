
from unuA import citire_matrice
from unuB import multimi

mat = citire_matrice("matrice.in")
N = len(mat)

positives = multimi(mat, N-3, N-2, N-1)[1]
negatives = multimi(mat, 0, N-1)[0]

print(*sorted(positives))
print(len(negatives))
