class graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={v : [] for v in range(vno)}

    def add_edge(self,v,u,weight=1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[v].append((u,weight))
            self.adj_list[u].append((v,weight))
         
        else:
            print("invalid vertices")


    def remove_edge(self,v,u):     
        if 0<=v<self.vertex_count and 0<=u<self.vertex_count:
            self.adj_list[v]=[(vertex,weight) for vertex,weight in self.adj_list  if self.vertex_count!=u]
            self.adj_list[u]=[(vertex,weight) for vertex,weight in self.adj_list  if self.vertex_count!=v]    
           
        else:
            print("invalid vertices")


    def has_edge(self,v,u):        
       if 0<=v<self.vertex_count and 0<=u<self.vertex_count:
           return any(vertex==u for vertex,x in self.adj_list[v]) 
       

    def print_graph(self):
        for vertex in range(self.vertex_count):
            print(f"Vertex {vertex}: {self.adj_list[vertex]}")

g =graph(5)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(3, 4)

g.print_graph()