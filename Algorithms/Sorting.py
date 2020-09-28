def PartitionR(list, l, r):
    v = list[r]
    i = l
    for j in range(l, r):
        if(list[j] < v):
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[r] = list[r], list[i]
    return i


def QuickSortR(list, l, r):
    if(l >= r):
        return
    i = PartitionR(list, l, r)
    QuickSortR(list, l, i-1)
    QuickSortR(list, i+1, r)


def PartitionL(list, l, r):
    X = list[l]
    i = l
    for j in range(l+1, r+1):
        if(list[j] < X):
            i += 1
            list[i], list[j] = list[j], list[i]
    list[l], list[i] = list[i], list[l]
    return i


def QuickSortL(list, l, r):
    if(l >= r):
        return
    i = PartitionL(list, l, r)
    QuickSortL(list, l, i-1)
    QuickSortL(list, i+1, r)


a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
QuickSortR(a, 0, len(a)-1)
print(a)
