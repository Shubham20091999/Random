from requests.api import head


class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r


class BinaryTree:
    def __init__(self, a: list = []):
        if(len(a) == 0):
            self.head = None
        else:
            self.head = Node(a[0])
            for e in a[1:]:
                self.insert(e)

    # https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/
    def insert(self, val):
        if(self.head == None):
            self.head = Node(val)
            return
        q = [self.head]
        while q:
            temp = q.pop(0)
            if(temp.left == None):
                temp.left = Node(val)
                break
            else:
                q.append(temp.left)

            if(temp.right == None):
                temp.right = Node(val)
                break
            else:
                q.append(temp.right)

    def getDeepest(self):
        if(self.head == None):
            return None, None, None
        q = [self.head]
        ans = self.head
        parent = None
        isLeft = True
        while q:
            p = q.pop(0)
            if(p.left != None):
                q.append(p.left)
                ans = p.left
                parent = p
                isLeft = True
            if(p.right != None):
                q.append(p.right)
                ans = p.right
                parent = p
                isLeft = False

        return ans, parent, isLeft

    def delete(self, val):
        a, _, _ = self.getNode(val)
        if(a == None):
            raise Exception
        d, p, l = self.getDeepest()
        a.val = d.val
        if(l):
            p.left = None
        else:
            p.right = None

    def getNode(self, val):
        if(self.head == None):
            return None, None, None
        q = [self.head]
        while q:
            p = q.pop(0)
            if(p.left != None):
                if(p.left.val == val):
                    return p.left, p, True
                q.append(p.left)
            if(p.right != None):
                if(p.right.val == val):
                    return p.right, p, True
                q.append(p.right)
        return None, None, None

    @staticmethod
    def __getVal(root, ans):
        if(root == None):
            return
        BinaryTree.__getVal(root.left, ans)
        ans.append(root.val)
        BinaryTree.__getVal(root.right, ans)

    def getVal(self):
        ans = []
        BinaryTree.__getVal(self.head, ans)
        return ans


bt = BinaryTree([1, 2, 3, 4, 5, 6, 7,8])
print(bt.getVal())
bt.delete(3)
print(bt.getVal())
