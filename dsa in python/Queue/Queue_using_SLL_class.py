class Node:
  def __init__(self,item=None,next=None):
      self.item=item
      self.next=next
class Queue():
  def __init__(self):
    self.front=None
    self.rear=None
    self.item_count=0

  def is_empty(self):
    return self.front==None
  
  def enqueue(self,data):
    n=Node(data)
    if self.is_empty():
     self.front=n
     
    else: 
      self.rear.next=n
    self.rear=n  
    self.item_count+=1
  def dequeue(self):
    if self.is_empty():
       raise ImportError("empty Queue")
    elif self.front==self.rear:
      self.front=None
      self.rear=None
    else:
      self.front=self.front.next   
    self.item_count-=1
  def get_first(self):
    if not self.is_empty():
      return self.rear.item

  def get_last(self):
    if not self.is_empty():
      return self.front.item
        
  def size(self):
    return self.item_count
mylist=Queue()
mylist.enqueue(1)
mylist.enqueue(2)
mylist.enqueue(3)
mylist.enqueue(4)
mylist.enqueue(5)


print("size",mylist.size())

delete_item=mylist.dequeue()
print("delete item",delete_item)

print("front",mylist.get_first())
print("rear",mylist.get_last())
print("size",mylist.size())    