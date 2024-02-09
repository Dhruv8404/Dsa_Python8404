import math

class Rectangle:

    def __init__(self,length,bredth):
        self.length=length
        self.bredth=bredth
    
    def get_length(self):
        return self.length    
    def get_bredth(self):
        return self.bredth
    
    def set_bothset(self,length,bredth):
        if length >=0 and bredth >=0:
            self.length=length
            self.bredth=bredth
        else:
            print(f"if length,bredth is not -ve set it")

    def get_Area(self):
        return self.length * self.bredth
    
my_rec=Rectangle(10,20)
print("length::",my_rec.get_length())
print("bredth::",my_rec.get_bredth())   
print("Area::",my_rec.get_Area()) 
