def insertionSort(a):
    for i in range(len(a)):
        j = i
        while j > 0 and a[j-1] > a[j]:
            a[j-1], a[j] = a[j], a[j-1] 
            j=j-1
            yield a