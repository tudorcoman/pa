
def multimi(mat, *lines):
    negatives = set()
    positives = set()

    for line in lines:
        negative = set()
        pozitive = set()
        for elem in mat[line]:
            if elem < 0:
                negative.add(elem)
            elif elem > 0 and (elem % 10 == (ord(str(elem)[0]) - ord('0'))):
                pozitive.add(elem)

        if len(negatives) == 0:
            negatives = negative
        else:
            negatives = negatives.intersection(negative)

        positives = positives.union(pozitive)


    return negatives, positives



