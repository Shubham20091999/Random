from random import randrange


def Partition(list, l, r, ind):
    list[ind], list[l] = list[l], list[ind]
    v = list[l]
    i = l
    for j in range(l+1, r+1):
        if(list[j] < v):
            i += 1
            list[i], list[j] = list[j], list[i]
    list[l], list[i] = list[i], list[l]
    return i


def PartitionRight(list, l, r):
    return Partition(list, l, r, r)


def PartitionLeft(list, l, r):
    return Partition(list, l, r, l)


def PartitionRand(list, l, r):
    return Partition(list, l, r, randrange(l, r+1))


def QuickSortRight(list, l, r):
    if(l >= r):
        return
    i = PartitionRight(list, l, r)
    QuickSortRight(list, l, i-1)
    QuickSortRight(list, i+1, r)


def QuickSortLeft(list, l, r):
    if(l >= r):
        return
    i = PartitionLeft(list, l, r)
    QuickSortLeft(list, l, i-1)
    QuickSortLeft(list, i+1, r)


def QuickSortRand(list, l, r):
    if(l >= r):
        return
    i = PartitionRand(list, l, r)
    QuickSortRand(list, l, i-1)
    QuickSortRand(list, i+1, r)


def kthLargest(list, l, r, k):
    if(l >= r):
        return
    i = PartitionRand(list, l, r)
    if(i == k):
        return
    if(i < k):
        QuickSortLeft(list, i+1, r)
    else:
        QuickSortLeft(list, l, i-1)
