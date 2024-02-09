#using list


class STACK:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def push(self,data):
         self.items.append(data)
    def peek(self):
        return self.items[-1]  
    def pop(self):
        if not self.is_empty():
         self.items.pop()   
    def size(self):
        return len(self.items)        
mylist=STACK()

mylist.push(1)
mylist.push(2)
mylist.push(3)
print(mylist.items)

print(mylist.pop())
print(mylist.items)
print(mylist.peek())    