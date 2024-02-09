#stack implementation by inherting linked list

from SLL import *

class stack(SLL):
    def __init__(self):
        super().__init__()
        self.count_item=0

    def is_empty(self):
        return super().is_empty()

    def insert_first(self, data):
        super().insert_first(data)
        self.count_item+=1

    def pop(self):
       super().delete_first()
       self.count_item-=1
    def peek(self):
       return self.start.item
    
    def size(self):
       return self.count_item
    
mylist=stack()
mylist.insert_first(1)
mylist.insert_first(2)
mylist.insert_first(3)
print(mylist.size())
mylist.pop()
print(mylist.size())
print(mylist.peek())

