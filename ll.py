class node:
    def __init__(self,data):
        self.data=data
        self.ref=None

class linkedlist:
    def __init__(self):
        self.head=None

    def print_data(self):
        if self.head is None:
            print(0)

        else:
            n=self.head
            while n is not None:
                print(n.data)
                n=n.ref

    def add_begin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node

    def add_end(self,data):
        new_node=node(data)
        n=self.head
        while n is not None:
            if n.ref==None:
                n.ref=new_node
                break
            n=n.ref

    def add_at_index(self,data,x):
        new_node=node(data)
        n=self.head
        c=0
        while n is not None:
            c=c+1
            if c==x:
                new_node.ref=n.ref
                n.ref=new_node
                break
            n=n.ref
    
    def reverse_data(self):
        prev=None
        current=self.head
        while current:
            x=current.ref
            current.ref=prev
            prev=current
            current=x
        self.head=prev


        


ll1=linkedlist()
ll1.add_begin(10)
ll1.add_end(20)
ll1.add_at_index(30,2)

ll1.reverse_data()
ll1.print_data()
