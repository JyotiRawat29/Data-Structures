#%%
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def insertEdge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, startNode):
        visited = set()
        st = []
        st.append(startNode)
        visited.add(startNode)

        #while(len(st)):
        while(st):
            #cur = st[-1] # storing last element
            #st.pop() # removing last element
            cur = st.pop() # removing and storing last element
            print(cur, end=" ")
            #if (cur not in visited):
             #   print(cur, end=" ")
              #  visited.add(cur)
            
            for vertex in self.graph[cur]:
                if(vertex not in visited):
                    st.append(vertex)
                    visited.add(vertex)

g = Graph()
g.insertEdge(2,1)
g.insertEdge(2,5)
g.insertEdge(5,6)
g.insertEdge(5,7)
g.insertEdge(1,9)
g.insertEdge(1,4)
g.dfs(2)