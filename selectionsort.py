def selectionSort(a):
    for i in range(len(a)):
        minpos = i
        for j in range(i, len(a)):
            if a[j] < a[minpos]:
                minpos = j
        
        a[i], a[minpos] = a[minpos], a[i]
        yield a
