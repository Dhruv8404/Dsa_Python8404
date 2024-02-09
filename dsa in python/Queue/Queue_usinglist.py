class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
       return len(self.items) ==0     
    
    def enqueue(self,data):
       self.items.append(data) 
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Error: Queue is empty.")
            return None

    def get_front(self):
       
      return self.items[0]
    
    def get_rear(self):
       
      return self.items[-1]
    
    def size(self):
      return len(self.items)      
         
mylist=Queue()
mylist.enqueue(1)
mylist.enqueue(2)
mylist.enqueue(3)
mylist.enqueue(4)
mylist.enqueue(5)


print("size",mylist.size())

delete_item=mylist.dequeue()
print("delete item",delete_item)

print("front",mylist.get_front())
print("rear",mylist.get_rear())
print("size",mylist.size())
