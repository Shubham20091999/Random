class Node:
    def __init__(self, v, l=None, r=None):
        self.val = v
        self.left = l
        self.right = r


class BinaryTree:
    def __init__(self, arr: list = []):
        if(len(arr) == 0 or arr[0] == None):
            self.head = None
        else:
            self.head = Node(arr[0])
            prevNode = [self.head]
            i = 1
            try:
                while True:
                    p = prevNode.pop(0)
                    if(arr[i] != None):
                        p.left = Node(arr[i])
                        prevNode.append(p.left)
                    i += 1
                    if(arr[i] != None):
                        p.right = Node(arr[i])
                        prevNode.append(p.right)
                    i += 1
            except IndexError:
                pass

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

    def listForm(self):
        q = [self.head]
        ans = [self.head.val]
        temp = []
        while q:
            while q:
                p = q.pop(0)

                if(p.left != None):
                    ans.append(p.left.val)
                    temp.append(p.left)
                else:
                    ans.append(None)
                if(p.right != None):
                    ans.append(p.right.val)
                    temp.append(p.right)
                else:
                    ans.append(None)
            q, temp = temp, q
        i = len(ans)-1
        for i in range(len(ans)-1, -1, -1):
            if(ans[i] != None):
                break
        del ans[i+1:]
        return ans

    def __repr__(self):
        return str(self.listForm())

    def getDeepest(self):
        # BFS
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

    @staticmethod
    def __dft_preorder_helper(node, ans):
        if(node == None):
            return
        ans.append(node.val)
        BinaryTree.__dft_preorder_helper(node.left, ans)
        BinaryTree.__dft_preorder_helper(node.right, ans)

    def dft_preorder_recursive(self):
        ans = []
        BinaryTree.__dft_preorder_helper(self.head, ans)
        return ans

    @staticmethod
    def __dft_postorder_helper(node, ans):
        if(node == None):
            return
        BinaryTree.__dft_postorder_helper(node.left, ans)
        BinaryTree.__dft_postorder_helper(node.right, ans)
        ans.append(node.val)

    def dft_postorder_recursive(self):
        ans = []
        BinaryTree.__dft_postorder_helper(self.head, ans)
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
            if(curr.left != None):
                pre = curr.left
                while pre.right != None and pre.right != curr:
                    pre = pre.right
                if(pre.right == None):
                    ans.append(curr.val)
                    pre.right = curr
                    curr = curr.left
                else:
                    pre.right = None
                    curr = curr.right
            else:
                ans.append(curr.val)
                curr = curr.right
        return ans

    def dft_postorder_iterative(self):
        # Do opposite of preOrder
        ans = []
        curr = self.head
        while curr:
            if(curr.right != None):
                pre = curr.right
                while(pre.left != None and pre.left != curr):
                    pre = pre.left
                if(pre.left == None):
                    pre.left = curr
                    ans.insert(0, curr.val)
                    curr = curr.right
                else:
                    curr = curr.left
                    pre.left = None
            else:
                ans.insert(0, curr.val)
                curr = curr.left
        return ans

    @staticmethod
    def invert_helper(node):
        if(node == None):
            return
        node.left, node.right = node.right, node.left
        BinaryTree.invert_helper(node.left)
        BinaryTree.invert_helper(node.right)

    def invert_recursive(self):
        BinaryTree.invert_helper(self.head)

    def invert_iterative(self):
        stack = [self.head]
        while stack:
            p = stack.pop(-1)
            p.left, p.right = p.right, p.left
            if(p.left):
                stack.append(p.left)
            if(p.right):
                stack.append(p.right)


# bt = BinaryTree([1, 2, 3, None, None, 6, 7, 8, 9, 10,
#                  None, 11, 12, None, None, None, 13])
# bt.invert_recursive()
# print(bt)
# bt.invert_iterative()
# print(bt)
