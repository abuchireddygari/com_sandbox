class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def set_data(self,data):
        self.data=data
    
    def set_next(self,next):
        self.next=next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

class ListSorted:
    def __init__(self):
        self.head=None
    
    def add_data(self,data):
        curr_node=self.head
        prev_node=None
        stop=False

        while curr_node!=None and not stop:
            if curr_node.get_data()>data:
                stop=True
            else:
                prev_node=curr_node
                curr_node=curr_node.get_next()

        node=Node(data)
        if prev_node==None:
            node.set_next(self.head)
            self.head=node
        else:
            node.set_next=prev_node.get_next()
            prev_node.set_next(curr_node.get_next())
            





