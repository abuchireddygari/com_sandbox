class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
    
    def set_next(self,new_next):
        self.next=new_next

    def set_data(self,new_data):
        self.data=new_data

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class LinkList:
    def __init__(self):
        self.head=None

    def add_data(self,data):
        n=Node(data)
        n.set_next(self.head)
        self.head=n

    def traverse(self):
        current=self.head
        while current.next!=None:
            print(current.get_data())
            current=current.get_next()
        print(current.get_data())
    
    def count(self):
        current=self.head
        count=0
        while current.next!=None:
            count=count+1
            current=current.get_next()
        print("count is",count)

ll=LinkList()
ll.add_data(31)
ll.add_data(77)
ll.add_data(17)
ll.add_data(93)
ll.add_data(26)
ll.add_data(54)
ll.traverse()
ll.count()



    