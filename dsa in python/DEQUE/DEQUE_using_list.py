class DEQUE:
    def __init__(self):
        self.items=[]

    def is_empty(self):
      return len(self.items)==0

    def insert_front(self,data):
             # Insert data at the beginning of the list
     self.items.insert(0, data)
    def insert_rear(self, data):
     
        self.items.append(data)   

    def delete_front(self):
     if not self.is_empty():
      return self.items.pop(0)
    
    def delete_rear(self):
       if not self.is_empty():
          return self.items.pop(-1)
       
    def size(self):
       return len(self.items) 
    
    def get_front(self):
       
      return self.items[-1]
    
    def get_rear(self):
       
      return self.items[0]
    def print_list(self):
        print("Deque elements:", end=" ")
        for item in self.items:
            print(item, end=" -> ")
       
mylist=DEQUE()
mylist.insert_front(1)
mylist.insert_front(2)
mylist.insert_front(3) 
mylist.insert_rear(4)
mylist.insert_rear(5)
print(mylist.print_list())
mylist.delete_front()
mylist.delete_rear()
print(mylist.get_front())
print(mylist.get_rear())
print(mylist.print_list())
print(mylist.size())
