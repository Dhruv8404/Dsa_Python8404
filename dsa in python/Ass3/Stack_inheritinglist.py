#by inherting list


class STACK(list):
    def is_empty(self):
        return len(self)==0
    def push(self,data):
        return self.append(data)
    def pop(self):
        return super().pop()
    def peek(self):
        return self[-1]  
    def insert(self):
        raise AttributeError ("no insert value in stack")
    
mylist=STACK()
mylist.push(10)
mylist.push(20) 
mylist.push(30)
print(mylist)
mylist.pop()
print(mylist)
print(mylist.peek())
print(mylist)
 
