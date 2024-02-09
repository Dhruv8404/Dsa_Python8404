class Graph:
    def __init__(self,vro):
        self.vartex_count=vro
        self.adj_matrix=[ [0]*vro for e in range(vro)]

    def add_edge(self,v,u,weight=1):
        if 0<=v<self.vartex_count and 0<=u<self.vartex_count:  
         self.adj_matrix[v][u]=weight
         self.adj_matrix[u][v]=weight
        else:  
           print("invalid vartex")

    def remove_edge(self,v,u):  
       if 0<=u<self.vartex_count and 0<=v<self.vartex_count:
          self.adj_matrix[v][u]=0
          self.adj_matrix[u][v]=0

       else:
          print("invalid vertices")   

    def has_edge(self,v,u):
        if 0<=u<self.vartex_count and 0<=v<self.vartex_count:
          return self.adj_matrix[u][v]!=0
        else:
           print("invalid vertices")
    def print_adj_matrix(self):       
       for e in self.adj_matrix:
        print(" ".join(map(str,e)))

mylist=Graph(5)
mylist.add_edge(0,1)
mylist.add_edge(1,2)
mylist.add_edge(1,3)
mylist.add_edge(2,4)
mylist.add_edge(2,5)
mylist.print_adj_matrix()
