#using linked list

class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class stack:
    def __init__(self):
        self.start=None
        self.item_count=0

    def is_empty(self):
        return self.start is None

    def push(self,data):
      n=Node(data)
      if not self.is_empty():
          
          n.next=self.start
      self.start=n
      self.item_count+=1

    def pop(self):
        if not self.is_empty():
            self.start=self.start.next
            self.item_count-=1

    def peek(self):
         if not self.is_empty():
             return self.start.data

    def size(self):
        return self.item_count

    def print_stack(self):
        if self.is_empty():
            print("Stack is empty.")
            return

        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

mylist=stack()

mylist.push(10)
mylist.push(20)
mylist.push(30)
print(mylist.print_stack())
print()
mylist.pop()

print(mylist.peek())
print(mylist.size())

