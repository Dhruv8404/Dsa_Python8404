class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class SLL:
    def __init__(self,start=None):
           self.start=start

    def is_empty(self):
         return self.start is None

    def insert_first(self,data):
         n=Node(data, self.start)
         self.start=n       

    def insert_last(self,data):
         n=Node(data) 
         if not self.is_empty():
              temp=self.start
              while temp.next is not None:
                   temp=temp.next
              temp.next=n
         else:
             self.start=n 

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print() 

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            
            temp = temp.next
            
        return None 
    def insert_after(self,temp,data):
       if temp is not None:
          n=Node(data,temp.next)
          temp.next=n

    def delete_first(self):
        if not self.is_empty():
            self.start = self.start.next
    
    def delete_last(self):
     if self.start is None:
        return  # Empty list, nothing to delete
     elif self.start.next is None:
        self.start = None  # Only one element in the list
     else:
        temp = self.start
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
     
  
    def delete_item(self, data):
     if self.start is None:
        return  # Empty list, nothing to delete
     elif self.start.item == data:
        self.start = self.start.next
     else:
        temp = self.start
        while temp.next is not None and temp.next.item != data:
            temp = temp.next
        if temp.next is not None:
            temp.next = temp.next.next


mylist = SLL()
mylist.insert_first(10)
mylist.insert_first(10)
mylist.insert_last(20)
mylist.insert_last(30)

mylist.insert_last(40)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
result = mylist.search(50)
if result:
     print("search::",result.item)
else:
     print("Not found")     



#mylist.delete_first()

#mylist.delete_last()

mylist.delete_item(20)
mylist.print_list()

