
def insertionSort(v):
    for i in range(1, len(v)):
        var = v[i]
        j = i - 1
        while j >= 0 and var < v[j]:
            v[j + 1] = v[j]
            j -= 1
        v[j + 1] = var

def bucketSort(v):
    maxValue = max(v)
    size = maxValue / len(v)

    buckets = []
    for i in range(len(v)):
        buckets.append([])
    
    for i in range(len(v)):
        j = int(v[i] / size)
        if j != len(v):
            buckets[j].append(v[i])
        else:
            buckets[len(v) - 1].append(v[i])

    for z in range(len(v)):
        insertionSort(buckets[z])
   
    output = []
    for i in range(len(v)):
        output = output + buckets[i]
    return output


sir = [10, 9, 7, 3, 4, 2, 1, 5, 6, 8]
print(bucketSort(sir)) 
