class Node:
    def __init__(self,item=None,priority=None,next=None):
        self.item=item
        self.next=next
        self.priority=priority  
class priorityqueue:
    def __init__(self):
        self.start=None
        self.item_count=0

    def is_empty(self):
        return self.start is None 
        
    def push(self,data,priority):
        n=Node(data,priority)
        if not self.start  or priority<self.start.priority: #insert first node only   but only 1st node 
            n.next=self.start
            self.start=n
        else:
            temp=self.start
            while  temp.next and temp.next.priority<=priority:
                    temp=temp.next
            n.next=temp.next
            temp.next=n 
        self.item_count+=1
    def pop(self):               
        if self.is_empty():
          raise IndexError("empty")
        
        data =self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data 
    def size(self):
       return self.item_count

mylist = priorityqueue()
mylist.push("dhruv", 1)
mylist.push("aman", 2)
mylist.push("raha", 3)
mylist.push("alak", 4)

while not mylist.is_empty():
    print(mylist.pop())
       
print(mylist.size())       