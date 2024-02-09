class Node:
    def __init__(self, prev=None, item=None, next=None):
        self.prev = prev
        self.item = item
        self.next = next

class CDLL:
    def __init__(self ,start=None):     

        self.start = start

    def is_empty(self):
        return self.start ==  None

    def insert_first(self, data):
        n = Node(item=data)

        if self.is_empty():
            n.next = n
            n.prev = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

        self.start = n

    def insert_last(self, data):
        n = Node(item=data)

        if self.is_empty():
            n.next = n
            n.prev = n
            self.start = n
        else:
            n.next = self.start
            n.prev = self.start.prev
            self.start.prev.next = n
            self.start.prev = n

    def search(self, data):
        temp = self.start
        if temp==None:
           return None
        if temp.item==data:
           return temp
        else: 
         temp=temp.next 
         while temp != self.start:
            if temp.item == data:
                return temp
            temp = temp.next
         return None
    

    def insert_item(self,temp,data):
       if temp is not None:
          
        n=Node(item=data)
        n.next=temp.next
        n.prev=temp
        temp.next.prev=n
        temp.next=n


   
    
    

    def delete_first(self):
     if not self.is_empty():
        if self.start.next == self.start:  # If there is only one element in the list
            self.start = None
        else:
            self.start.prev.next = self.start.next
            self.start.next.prev = self.start.prev
            self.start = self.start.next

    def delete_last(self):
        if not self.is_empty():
            if self.start.next == self.start:  # If there is only one element in the list
                self.start = None
            else:
                self.start.prev.prev.next = self.start
                self.start.prev = self.start.prev.prev
    
    def delete_item(self,data):
        if self.is_empty():
            print("Cannot delete from an empty list.")
            return

        temp = self.start
        while True:
            if temp.item == data:
                if temp.next == temp:  # If there's only one element
                    self.start = None
                else:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    if temp == self.start:  # If deleting the first element
                        self.start = temp.next
                print(f"Deleted item: {data}")
                return
            temp = temp.next
            if temp == self.start:
                break

        print(f"Item {data} not found in the list.")

    def print(self):
        temp = self.start
        if not self.is_empty():
            while True:
                print(temp.item, end=' ')
                temp = temp.next
                if temp == self.start:
                    break
            print()


# Rest of your code...

mylist = CDLL()
mylist.insert_first(10)
mylist.insert_first(5)



mylist.insert_last(20)
mylist.insert_last(30)
mylist.insert_last(40)
mylist.insert_last(50)
mylist.insert_last(60)
mylist.insert_item(mylist.search(5),45)


mylist.print()


mylist.delete_first()
mylist.print()



mylist.delete_last()
mylist.delete_item(50)
mylist.print()

