#%%
"""
undirected means bidirectional
"""
class Graph():
    def __init__(self, number_of_nodes):
        self.number_of_nodes = number_of_nodes + 1
        self.graph = [[0 for i in range(self.number_of_nodes)] for j in range(self.number_of_nodes)]
    
    def withinBounds(self,v1,v2):
        return((v1>=0 and v1<=self.number_of_nodes) and 
               (v2>=0 and v2<=self.number_of_nodes))
    
    def insertEdges(self,v1,v2):
        if self.withinBounds(v1,v2):
            self.graph[v1][v2] = 1
            self.graph[v2][v1] = 1
   
    def printGraph(self):
        print(self.graph)

g = Graph(5)
g.insertEdges(1,2)
g.insertEdges(1,3)
g.insertEdges(2,4)
g.insertEdges(3,5)
g.printGraph()
# %%
