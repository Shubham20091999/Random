class Node:
    def __init__(self, val, nxt=None) -> None:
        self.val = val
        self.nxt = nxt

    def __repr__(self) -> str:
        return str(self.val)

    def __str__(self) -> str:
        return str(self.val)


class LinkedList:
    # So many if statements bcuz the Location in memory changes if the type in converted from Node to None
    def __init__(self, arr=[]) -> None:
        if(len(arr) == 0):
            # better initilize as Node(None,None)
            # As when changing the next node from None the memory changes
            # But most of the problems initilize as None
            self.head = None
        else:
            self.head = Node(arr[0], None)
            h = self.head
            for i in range(1, len(arr)):
                h.nxt = Node(arr[i], None)
                h = h.nxt

    def __repr__(self) -> str:
        h = self.head
        s = ''
        while h != None:
            s += str(h)+' '
            h = h.nxt
        return s

    def getEnd(self) -> Node:
        h = self.head
        while h.nxt != None:
            h = h.nxt
        return h

    def insert_element(self, pos, val):
        try:
            if(pos == 0):
                self.head = Node(val, self.head)
            elif(pos == 1):
                # IndexError if(self.head == None):
                self.head.nxt = Node(val, self.head.nxt)
            elif(pos == -1):
                h = self.head
                if(h == None):
                    self.head = Node(val, None)
                elif(h.nxt == None):
                    self.head.nxt = Node(val, self.head.nxt)
                else:
                    while h.nxt != None:
                        h = h.nxt
                    h.nxt = Node(val, None)
            elif(pos > 1):
                # IndexError if(self.head == None):
                h = self.head.nxt
                pos -= 1
                while pos > 1:
                    h = h.nxt
                    pos -= 1
                h.nxt = Node(val, h.nxt)
            else:
                raise Exception
        except:
            raise IndexError

    def remove_index(self, pos):
        try:
            if(pos == 0):
                v = self.head.val
                self.head = self.head.nxt
                return v
            elif(pos == 1):
                # IndexError if(self.head == None or self.head.nxt == None):
                v = self.head.nxt.val
                self.head.nxt = self.head.nxt.nxt
                return v
            elif(pos == -1):
                # IndexError if(self.head == None):
                if(self.head.nxt == None):
                    v = self.head.val
                    self.head = None
                    return v
                else:
                    h = self.head
                    while h.nxt.nxt != None:
                        h = h.nxt
                    v = h.nxt.val
                    h.nxt = None
                    return v
            elif(pos > 1):
                h = self.head
                while pos > 1:
                    h = h.nxt
                    pos -= 1
                v = h.nxt.val
                h.nxt = h.nxt.nxt
                return v
            else:
                raise Exception
        except:
            raise IndexError('Index out of range')

    def reverse(self):
        # not(len=0 or 1)
        if(self.head != None and self.head.nxt != None):
            h = self.head
            nxt = self.head.nxt
            h.nxt = None
            while nxt != None:
                temp = nxt.nxt
                nxt.nxt = h
                h = nxt
                nxt = temp
            return h
        return self

    def getNode_index(self, pos, preNodeDiff=0, nxtNodeDiff=0):
        h = self.head
        preNode = self.head
        while pos > 0:
            h = h.nxt
            pos -= 1
            if(preNodeDiff == 0):
                preNode = preNode.nxt
            else:
                preNodeDiff -= 1
        if(preNodeDiff != 0):
            preNode = None
        nxtNode = h
        while nxtNodeDiff > 0 and nxtNode != None:
            nxtNode = nxtNode.nxt
            nxtNodeDiff -= 1
        if(nxtNodeDiff != 0):
            nxtNode = None
        return (h, preNode, nxtNode)


l = LinkedList([1])
print(l.getNode_index(0, 1, 1))
