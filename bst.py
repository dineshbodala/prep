class BST:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None

    def insert(self,data):
         if self.data==None:
             self.data=data
             return

         if self.data>data:
             if self.lchild:
                 self.lchild.insert(data)

             else:
                 self.lchild=BST(data)

         else:
             if self.rchild:
                 self.rchild.insert(data)

             else:
                 self.rchild=BST(data)

    def search(self,data):
        if self.data==data:
            print(1)
            return

        if self.data>data:
            if self.lchild:
                self.lchild.search(data)

            else:
                print(0)

        else:
            if self.rchild:
                self.rchild.search(data)

            else:
                print(0)
root=BST(10)
x=[11,1,12,2,13,3]
for i in x:
    root.insert(i)

root.search(200)

