import math

class circle:
    
   def __init__(self,radius):
        self.radius=radius
   
   def get_circle(self):
        return self.radius 
   
   def set_circle(self,radius):
       if radius >=0 :
           self.radius = radius
       else:
           print(f"that nagative is not allow set radius")
   def get_Area(self):
       return math.pi * self.radius **2
   
   def get_Circumference(self):
       return 2 * math.pi * self.radius
   
my_data=circle(10.0)
print("Circle::",my_data.get_circle())
print("Area::",my_data.get_Area()) 
print("Circumference::",my_data.get_Circumference())  