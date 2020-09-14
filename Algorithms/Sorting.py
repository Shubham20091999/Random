def QuickSort(list,l,r):
    if(l>=r):
        return
    v=list[r]
    i=l
    for j in range(l,r):
        if(list[j]<v):
            list[i],list[j]=list[j],list[i]
            i+=1
    list[i],list[r]=list[r],list[i]
    QuickSort(list,l,i-1)
    QuickSort(list,i+1,r)
a=[9,8,7,6,5,4,3,2,1,0]
QuickSort(a,0,len(a)-1)
print(a)
