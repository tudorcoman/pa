def mat_tri(n):
    m = [[0] * i for i in range(1, n + 1)]

    for i in range(n):
        m[i][0] = i + 1
        m[n - 1][i] = n - i

    for i in range(n - 2, 0, -1):
        for j in range(1, i + 1):
            m[i][j] = m[i + 1][j] + m[i + 1][j - 1] + m[i][j - 1]

    return m

def afis(M):
    ncmax = max([len(str(max(linie))) for linie in M])
    for linie in M:
        for elem in linie:
            print(str(elem).rjust(ncmax), end=' ')
        print()
    
print(mat_tri(4))
afis(mat_tri(4))


