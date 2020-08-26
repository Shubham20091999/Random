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
    def __init__(self, arr: list = []) -> None:
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

    @staticmethod
    def initilize(node: Node):
        l = LinkedList()
        l.head = node
        return l

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

    def len(self):
        l=0
        h=self.head
        while h!=None:
            l+=1
            h=h.nxt
        return l

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
            return LinkedList.initilize(h)
        return self

    def getNode_element(self, val, preNodeDiff=0):
        if(preNodeDiff < 0):
            raise IndexError('Diff should be positive')
        try:
            h = self.head
            preNode = self.head
            pos = 0
            while h.val != val:
                pos += 1
                h = h.nxt
                if(preNodeDiff == 0):
                    preNode = preNode.nxt
                else:
                    preNodeDiff -= 1
            if(preNodeDiff != 0):
                preNode = None
            return (pos, h, preNode)
        except:
            raise ValueError('Value not found in the list')

    def getNode_index(self, pos, preNodeDiff=0):
        if(preNodeDiff < 0):
            raise IndexError('Diff should be positive')
        try:
            h = self.head
            preNode = self.head
            if(pos >= 0):
                while pos > 0:
                    h = h.nxt
                    pos -= 1
                    if(preNodeDiff == 0):
                        preNode = preNode.nxt
                    else:
                        preNodeDiff -= 1
            elif(pos == -1):
                while h.nxt != None:
                    h = h.nxt
                    if(preNodeDiff == 0):
                        preNode = preNode.nxt
                    else:
                        preNodeDiff -= 1
            else:
                raise Exception

            if(preNodeDiff != 0):
                preNode = None
            return (h, preNode)
        except:
            raise IndexError('Index out of range')

    def remove_element(self, e):
        pos, node, prenode = self.getNode_element(e, 1)
        if(prenode == None):
            self.head = self.head.nxt
        else:
            prenode.nxt = node.nxt
        return pos

    def remove_index(self, pos):
        node, prenode = self.getNode_index(pos, 1)
        if(prenode == None):
            self.head = self.head.nxt
        else:
            prenode.nxt = node.nxt

    def insert_element(self, pos, val):
        node, prenode = self.getNode_index(pos, 1)
        if(prenode == None):
            self.head = Node(val, self.head)
        elif(pos == -1):
            node.nxt = Node(val, None)
        else:
            prenode.nxt = Node(val, node)
