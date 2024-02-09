class Book:
    def __init__(self,Bookid=None,title=None,price=None):
        self.Bookid=Bookid
        self.title=title
        self.price=price

    def show(self):
       print("BookID::",self.Bookid)
       print("title::",self.title)
       print("price::",self.price)
book_data=Book(1,"gita",100)
print(book_data.show())       
    