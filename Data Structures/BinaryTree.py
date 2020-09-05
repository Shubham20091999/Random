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
            BinaryTree.__helper(a[1:], [self.head])

    @staticmethod
    def __helper(arr, prevNodeArr):
        if(len(arr) == 0):
            return
        currActiveNodes = []
        for p in prevNodeArr:
            if(len(arr) == 0):
                break
            if(arr[0] != None):
                p.left = Node(arr[0])
                currActiveNodes.append(p.left)
            arr.pop(0)
            if(len(arr) == 0):
                break
            if(arr[0] != None):
                p.right = Node(arr[0])
                currActiveNodes.append(p.right)
            arr.pop(0)
        else:
            BinaryTree.__helper(arr, currActiveNodes)

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

    def bft(self):
        q = [self.head]
        ans = []
        temp = []
        while q:
            ans.append([e.val for e in q])
            while q:
                p = q.pop(0)
                if(p.left != None):
                    temp.append(p.left)
                if(p.right != None):
                    temp.append(p.right)
            q, temp = temp, q
        return ans

    @staticmethod
    def __dft_inorder_helper(node, ans):
        if(node == None):
            return
        BinaryTree.__dft_inorder_helper(node.left, ans)
        ans.append(node.val)
        BinaryTree.__dft_inorder_helper(node.right, ans)

    def dft_inorder_recursive(self):
        ans = []
        BinaryTree.__dft_inorder_helper(self.head, ans)
        return ans

    # $$$$$$$$$$$$$$$
    def dft_inorder_iterative(self):
        # Space - O(1)
        # Time - O(n) (n=number of nodes)
        curr = self.head
        ans = []
        while curr:
            if(curr.left != None):
                pre = curr.left
                while (pre.right != None) and pre.right != curr:
                    pre = pre.right
                if(pre.right == None):
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    ans.append(curr.val)
                    curr = curr.right
            else:
                ans.append(curr.val)
                curr = curr.right
        return ans

    def dft_preorder_iterative(self):
        ans = []
        curr = self.head
        while curr:
            ans.append(curr.val)
            if(curr.left != None):
                pre = curr.left
                while pre.right != None and pre.right != curr.right:
                    pre = pre.right
                if(pre.right == None):
                    pre.right = curr.right
                    curr = curr.left
                else:
                    pre.right = None
                    curr = curr.right
            else:
                curr = curr.right
        return ans


bt = BinaryTree([1, None, 2])
print(bt.dft_inorder_recursive())
