class priorityqueue:
    def  __init__(self):
        self.items=[]

    def push(self,data,priority):
     index=0    
     while index<len(self.items) and  self.items[index][1]<=priority: # [1] this is index index is check index[1]->[2]->[3]go on
        index+=1
     self.items.insert(index,(data,priority))  #()this is tupple(data,priority) this only
        
    def is_empty(self):
        return len(self.items)==0

    def pop(self):
       if not self.is_empty():
           return self.items.pop(0)[0]
       
    def size(self):
        return len(self.items)   