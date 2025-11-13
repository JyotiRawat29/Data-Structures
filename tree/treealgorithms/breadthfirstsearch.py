from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def setEdge(self,u,v):
        self.graph[u].append(v)
    
    def bfs(self,root):
        visited = set()
        queue = []
        queue.append(root)
        visited.add(root)
        
        while queue:
            u = queue.pop(0) #remove the 1st element
            print(u, end=" ")

            for v in self.graph[u]:
                if v not in visited:
                    queue.append(v) #adding at last
                    visited.add(v)

g = Graph()
g.setEdge(2,1)
g.setEdge(2,5)
g.setEdge(5,6)
g.setEdge(5,8)
g.setEdge(1,9)

g.bfs(2)