class Queue(list):
    
    def is_empty(self):
        return len(self)==0
    
    def enqueue(self,data):
        self.append(data)
    
    def dequeue(self):
        if not self.is_empty():
            return self.pop(0)
        else:
            print("Error: Queue is empty.")
            return None
    def get_first(self):
        if not self.is_empty():
            return self[0]

    def get_last(self):
        return self[-1]
    

    def size(self):
        return len(self)   
    

mylist=Queue()
mylist.enqueue(1)
mylist.enqueue(2)
mylist.enqueue(3)
mylist.enqueue(4)
print(mylist.size())
mylist.dequeue()
print(mylist.get_first())
print(mylist.get_last())
print(mylist.size())