class maxheap:
    # n->number of nodes

    # log(n)
    def heapify_down(self, i):
        v = i
        l = 2*i+1
        r = 2*i+2
        if(l < len(self.lst) and self.lst[v] < self.lst[l]):
            v = l
        if(r < len(self.lst) and self.lst[v] < self.lst[r]):
            v = r
        if(v != i):
            self.lst[i], self.lst[v] = self.lst[v], self.lst[i]
            self.heapify_down(v)

    # log(n)
    def heapify_up(self, i):
        if(i != 0):
            v = (i-1)//2
            if(self.lst[v] < self.lst[i]):
                self.lst[i], self.lst[v] = self.lst[v], self.lst[i]
                self.heapify_up(v)

    # n
    def build(self):
        for i in range(len(self.lst)//2, -1, -1):
            self.heapify_down(i)

    # 1
    def peek(self):
        return self.lst[0]

    # log(n)
    def pop(self):
        ret = self.peek()
        self.lst[0], self.lst[-1] = self.lst[-1], self.lst[0]
        self.lst.pop(-1)
        self.heapify_down(0)
        return ret

    # log(n)
    def push(self, v):
        self.lst.append(v)
        self.heapify_up(len(self.lst)-1)

    # n
    def replace(self, p, v):
        i = self.lst.index(p)
        self.lst[i] = v
        if(p > v):
            self.heapify_down(i)
        else:
            self.heapify_up(i)

    # log(n)
    def insert_extract(self, v):
        if(self.peek() > v):
            self.lst[0], v = v, self.lst[0]
            self.heapify_down(0)
        return v

    def __init__(self, lst: list) -> None:
        self.lst = lst
        self.build()
        print(self.lst)


h = maxheap([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(h.lst)
h.replace(1, 20)
print(h.lst)
