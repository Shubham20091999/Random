from os import close


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


class Dij(Graph):
    def __init__(self, n, lst) -> None:
        self.size = n
        self.graph = [[] for _ in range(n)]
        self.wt = {}
        for e in lst:
            self.graph[e[0]].append(e[1])
            self.graph[e[1]].append(e[0])
            self.wt[(e[0], e[1])] = e[2]
            self.wt[(e[1], e[0])] = e[2]
            
    def search(self, head, tail):
        dist = [float('inf')] * self.size
        dist[head] = 0
        parent = [None]*self.size
        closed = [False]*self.size
        while(True):
            p = -1
            m = float('inf')
            for i, d in enumerate(dist):
                if(closed[i]==False):
                    if(d < m):
                        p = i
                        m = d
            closed[p]=True
            if(p == tail):
                break
            for child in self.graph[p]:
                if(dist[child] > dist[p]+self.wt[(p, child)]):
                    dist[child] = dist[p]+self.wt[(p, child)]
                    parent[child] = p
        ans=[tail]
        while True:
            if(parent[ans[0]]):
                ans.insert(0,parent[ans[0]])
            else:
                break
        ans.insert(0,head)
        return ans

# g = Dij(5, [(0, 4), (0, 1), (1, 4), (1, 3), (2, 3)])
# print(g.search(0,2))

edges=[(0,1,7),(0,2,2),(1,2,3),(2,4,10),(4,5,6),(0,6,7),(6,7,3),(6,8,12),(7,8,8),(8,5,5),(1,3,4),(2,3,4),(3,4,3)]
d = Dij(9,edges)
d.search(0,5)
