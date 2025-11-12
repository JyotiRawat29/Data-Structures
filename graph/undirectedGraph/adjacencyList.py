#%%
from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)
    
    def insertEdges(self, v1, v2):
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)
    
    def printGraph(self):
        print(self.graph)


g = Graph()
g.insertEdges(1,2)
g.insertEdges(1,3)
g.insertEdges(2,4)
g.insertEdges(3,5)
g.printGraph()
# %%
