from random import randrange

def PartitionRight(list, l, r):
    v = list[r]
    i = l
    for j in range(l, r):
        if(list[j] < v):
            list[i], list[j] = list[j], list[i]
            i += 1
    list[i], list[r] = list[r], list[i]
    return i

def PartitionLeft(list, l, r):
    v = list[l]
    i = l
    for j in range(l+1, r+1):
        if(list[j] < v):
            i += 1
            list[i], list[j] = list[j], list[i]
    list[l], list[i] = list[i], list[l]
    return i


def PartitionRand(list,l,r):
    t=randrange(l,r+1)
    list[t],list[l]=list[l],list[t]
    return PartitionLeft(list,l,r)

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

def QuickSortRand(list,l,r):
    if(l>=r):
        return
    i=PartitionRand(list,l,r)
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

a = [3,14, 17, 13, 15, 19, 10, 3, 16, 9, 12]
QuickSortRand(a,0,len(a)-1)
print(a)


