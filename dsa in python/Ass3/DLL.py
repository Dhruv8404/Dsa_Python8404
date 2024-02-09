class Node:
    def __init__(self,prev=None,item=None,next=None):
       self.prev=prev
       self.item=item
       self.next=next
class DLL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_first(self, data):
        n = Node(None, data, self.start)

        if not self.is_empty():
            self.start.prev = n

        self.start = n

    def insert_last(self, data):
        temp = self.start

        if not self.is_empty():
            while temp.next is not None:
                temp = temp.next

            n = Node(temp, data, None)
            temp.next = n
        else:
            # The list is empty, insert the first node
            n = Node(None, data, None)
            self.start = n

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next

        return None

    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)

            if temp.next is not None:
                temp.next.prev = n

            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next

    def delete_first(self):
        if self.is_empty():
            return None
        elif self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.prev = None

    def delete_last(self):
        if self.is_empty():
            return None
        elif self.start.next is None:
            # Only one element in the list
            self.start = None
        else:
            # Traverse to the last node
            temp = self.start
            while temp.next is not None:
                temp = temp.next

            # Remove the last node
            temp.prev.next = None 
    def delete_item(self, data):
        temp = self.start

        while temp is not None:
            if temp.item == data:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                else:
                    self.start = temp.next

                if temp.next is not None:
                    temp.next.prev = temp.prev

                return

            temp = temp.next           

mylist = DLL()
mylist.insert_first(10)
mylist.insert_last(20)
mylist.insert_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.insert_after(mylist.search(30),35)
mylist.insert_after(mylist.search(35),40)
print("Original List:")
mylist.print_list()

mylist.delete_first()
print("\nAfter deleting the first element:")
mylist.print_list()

mylist.delete_last()
print("\nAfter deleting the last element:")
mylist.print_list()

mylist.delete_item(35)
print("\nAfter deleting the element:")
mylist.print_list()
