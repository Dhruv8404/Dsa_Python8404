from SLL import *

class STACK:
    def __init__(self):
        self.mylist = SLL()
        self.count_item = 0

    def is_empty(self):
        return self.mylist.is_empty()

    def push(self,data):
    
            self.mylist.insert_first(data)
            self.count_item += 1

    def pop(self):
        
            self.mylist.delete_first()
            self.count_item -= 1

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.item  # Return data, not item


    def size(self):
         return self.count_item    

s = STACK()
s.push(1)
s.push(2)
s.push(3)
print(s.peek())
s.pop()


print(s.size())