class Graph:
    def __init__(self, n, lst):
        # lst list of edges
        # n number of nodes
        self.size = n
        self.graph = [[] for _ in range(n)]
        for edge in lst:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

    def BFS_Tree(self, head=0):
        openNodes = [head]
        visited = [False for _ in range(self.size)]
        visited[head] = True
        structure = [[] for _ in range(self.size)]
        while (len(openNodes)):
            for _ in range(len(openNodes)):
                p = openNodes.pop(0)
                for child in self.graph[p]:
                    if(not(visited[child])):
                        openNodes.append(child)
                        visited[child] = True
                        structure[p].append(child)
        return structure

    def BFS_Level(self, head=0):
        openNodes = [head]
        visited = [False for _ in range(self.size)]
        visited[head] = True
        structure = [[head]]
        level = 0
        while (len(openNodes)):
            structure.append([])
            for _ in range(len(openNodes)):
                p = openNodes.pop(0)
                for child in self.graph[p]:
                    if(not(visited[child])):
                        openNodes.append(child)
                        visited[child] = True
                        structure[level+1].append(child)
            level += 1
        if(len(structure[-1]) == 0):
            structure.pop(-1)
        return structure

    def DFS_Tree(self, head=0):
        stack = [head]
        structure = [[] for _ in range(self.size)]
        visited = [False for _ in range(self.size)]
        visited[head] = True
        while(len(stack)):
            p = stack[-1]
            for child in self.graph[p]:
                if(visited[child] == False):
                    stack.append(child)
                    structure[p].append(child)
                    visited[child] = True
                    break
            else:
                stack.pop(-1)
        return structure

g = Graph(5, [(0, 4), (0, 1), (1, 4), (1, 3), (2, 3)])
print(g.DFS_Tree(1))
