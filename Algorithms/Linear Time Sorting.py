def BinaryRadixSort(arr,m=32):
    i = 1
    temp = [None]*len(arr)
    for j in range(0, m):
        B = [0, 0]
        for n in arr:
            B[(n & i) >> j] += 1
        B[1] = B[0]
        B[0]=0
        for n in arr:
            tmpC=(n & i) >> j
            temp[B[tmpC]] = n
            B[tmpC] += 1
        arr, temp = temp, arr
        i <<= 1
    return arr




