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

    def preorder(self):
        print(self.data)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data)
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data)



root=BST(10)
x=[1,11,12,3,14,6,7]
for i in x:
    root.insert(i)
root.search(12)
print(root.inorder())
print('b')
print(root.preorder())
print('c')
print(root.postorder())


