class Node:
    def __init__(self,item=None,left=None,right=None):
       
        self.item=item
        self.left=left
        self.right=right

class BST:
    def __init__(self,root=None):
        self.root=root
        
    def insert(self,data):
        self.root=self.rinsert(self.root,data)
    def rinsert(self,root,data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left=self.rinsert(root.left,data)
        elif data > root.item:
            root.right=self.rinsert(root.right,data) 
        return root
    
    def search(self,data):
      return self.searching(self.root,data)
    
    def searching(self,root,data):
      if root is None or root.item==data:
          return root
      elif  data < root.item:
          return self.searching(self.left,data)
      else:
          return self.searching(self.right,data)       


    def inorder(self):
        result=[]
        self.rinorder(self.root,result)
        return result
    def rinorder(self,root,result):
        if root:
            result.append(root.item)
            self.rinorder(root.left,result)
            self.rinorder(root.right,result)

    def preorder(self):
        result=[]
        self.rpreorder(self.root,result)
        return result
    def rpreorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            result.append(root.item)
            self.rinorder(root.right,result)   
    def postorder(self):
        result=[]
        self.rpostorder(self.root,result)
        return result
    def rpostorder(self,root,result):
        if root:
            self.rinorder(root.left,result)
            self.rinorder(root.right,result)
            result.append(root.item)                

    def min_val(self,temp):
        
        while temp.left is not None:
           temp=temp.left
        return temp.item            
    
    def max_val(self,temp):
        current=temp
        while current.right is not None:
            current=current.right
        return current.item
    
    def delete(self,data):
        self.root=self.rdelete(self.root,data)

    def rdelete(self,root,data):
        if root is None:
            return None
        elif data< root.item:
           root.left=self.rdelete(root.left,data)    
        elif data>root.item:
          root.right=self.rdelete(root.right,data)
        else:        
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item=self.min_val(root.right)
            self.rdelete(root.right,root.item)
        return root

    def size(self):
      return  len(self.inorder())
    

mylist = BST()
mylist.insert(100)
mylist.insert(50)
mylist.insert(200)
mylist.insert(45)
mylist.insert(60)
mylist.insert(70)
mylist.insert(75)

print("Inorder Traversal:", mylist.inorder())
