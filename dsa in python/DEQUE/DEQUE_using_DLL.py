class Node:
    def __init__(self, item=None, prev=None, next=None):
        self.prev = prev       
        self.item = item
        self.next = next
       

class DEQUE:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):
        return self.item_count==0

    def insert_front(self, data):    
        n = Node(data,None,self.front)
        if self.is_empty():
            self.rear = n
        else:
            self.front.prev = n 
        self.front = n     
        self.item_count+= 1

    def insert_rear(self, data):
        n = Node(data,self.rear)
        if self.is_empty():
            self.front = n
        else:
            self.rear.next = n
        self.rear = n
        self.item_count+= 1

    def delete_front(self):
        
            if self.front == self.rear:
                self.rear = None
                self.front = None
            else:
                self.front = self.front.next
                self.front.prev==None                
            self.item_count-= 1
            
    def delete_rear(self):
         if self.front == self.rear:
                self.rear = None
                self.front = None
         else:
                 self.rear = self.rear.prev
                 self.rear.next = None
         self.item_count-= 1

    def get_front(self):
        if not self.is_empty():
            return self.front.item      

    def get_rear(self):
        if not self.is_empty():
            return self.rear.item

    def size(self):
        return self.item_count
    

mylist = DEQUE()
mylist.insert_front(1)
mylist.insert_front(2)
mylist.insert_front(3)
mylist.insert_front(4)
mylist.insert_rear(5)
mylist.insert_rear(6)

mylist.delete_front()  # Output: 4
mylist.delete_rear()
print(mylist.get_front())     # Output: 3
print(mylist.get_rear())      # Output: 6
print(mylist.size())          # Output: 5
