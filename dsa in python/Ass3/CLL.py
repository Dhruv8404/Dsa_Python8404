class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

class CLL:
    def __init__(self, last=None):
        self.last = last

    def is_empty(self):
        return self.last is None

    def insert_first(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n

    def insert_last(self, data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

    def print_list(self):
        if self.is_empty():
            print("Circular Linked List is empty.")
        else:
            temp = self.last.next
            while temp is not self.last:
                print(temp.item, end=" ")
                temp = temp.next
            print(temp.item)  # Print the last item

    def search(self, data):
        if self.is_empty():
            print("Circular Linked List is empty.")
            return None

        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next

        # Check the last node
        if temp.item == data:
            return temp

        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(data, temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n

    def __iter__(self):
        self.current = self.last.next
        return self

    def __next__(self):
        if self.is_empty() or self.current == self.last.next:
            raise StopIteration
        else:
            item = self.current.item
            self.current = self.current.next
            if self.current == self.last.next:  # Added to detect the end of iteration
                raise StopIteration
            return item
    def delete_first(self):
       temp=self.last.next
       if self.is_empty(): 
             pass
      
       elif self.last == temp:
             return self.last.next==0 
 
       else:
         
        self.last.next=temp.next                           
       
    def delete_last(self):
        if self.is_empty():
           pass
        
        elif self.last.next == self.last:
           return self.last==None
        else:
            temp=self.last.next
            while temp.next != self.last:
                temp=temp.next    
        temp.next=self.last.next
        self.last=temp    
          
    
                               
    
    def delete_item(self, data):
        if self.is_empty():
            print("Circular Linked List is empty.")
        else:
            temp = self.last.next
            prev = None

            while temp != self.last:
                if temp.item == data:
                    if prev:
                        prev.next = temp.next
                        if temp == self.last:
                            self.last = prev
                    else:
                        # Deleting the first node
                        self.last.next = temp.next
                        if temp == self.last:
                            self.last = self.last.next
                    return

                prev = temp
                temp = temp.next

            # Check the last node
            if temp.item == data:
                if prev:
                    prev.next = temp.next
                    if temp == self.last:
                        self.last = prev
                else:
                    # Deleting the only node in the list
                    self.last = None             
         
         
          
          

# Example usage:
mylist = CLL()
mylist.insert_last(30)
mylist.insert_last(40)
mylist.insert_last(50)
mylist.insert_first(10)
mylist.insert_first(20)
mylist.insert_after(mylist.search(50), 45)
mylist.print_list()

mylist.delete_first()
mylist.delete_last()
mylist.print_list()
mylist.delete_item(10)
mylist.print_list()
for x in mylist:
    print(x, end=' ')
print()


