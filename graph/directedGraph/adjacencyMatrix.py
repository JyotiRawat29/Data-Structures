""""
Number of nodes in a graph:
If a graph is said to have a 5 nodal graph than the number of nodes would be:
0,1,2,3,4,5.
# number of nodes = 6
It cannot have 6 or 7 as numbers/keys in the nodes
"""

class Graph():
    def __init__(self,number_of_nodes):
        self. number_of_nodes = number_of_nodes + 1
        self.graph = [[0 for i in range(self. number_of_nodes)] for j in range(self. number_of_nodes)]
    
    def withinBounds(self,v1,v2):
        return ((v1 >= 0 and v1 <=self.number_of_nodes) and 
                (v2>=0 and v2<=self. number_of_nodes))
    
    def insertEdge(self,v1,v2):
        if self.withinBounds(v1,v2):
            self.graph[v1][v2] = 1
    
    def printGraph(self):
        for node in range(self.number_of_nodes):
            for value in range(len(self.graph)):
                if self.graph[node][value]:
                    print(f"{node}-->{value}")
g = Graph(5)
g.insertEdge(1,2)
g.insertEdge(2,3)
g.insertEdge(4,5)
g.printGraph()
