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

class ListUnOrdered:
    
    def __init__(self):
        self.head=None
    
    def add_data(self,data):
        node=Node(data)
        node.set_next(self.head)
        self.head=node

    def traverse(self):
        
        if self.head==None:
            return None
        
        cur_node=self.head

        while cur_node!=None:
            print(cur_node.data)
            cur_node=cur_node.get_next()
            
    def count(self):
        cnt=0
        if self.head==None:
            return cnt
        
        cur_node=self.head

        while cur_node!=None:
            cnt=cnt+1
            cur_node=cur_node.get_next()

        return cnt
        
    def search(self,value):
        is_found=False
        if self.head==None:
            return is_found
        cur_node=self.head
        while cur_node!=None and not is_found:
            if cur_node.get_data()==value:
                is_found=True
            else:
                cur_node=cur_node.get_next()

        return is_found






list1=ListUnOrdered()
print(list1.count())
list1.traverse()
print(list1.search(20))
list1.add_data(10)
list1.add_data(20)
list1.add_data(30)
list1.add_data(40)
list1.add_data(50)
list1.add_data(60)
list1.add_data(70)
list1.traverse()
print(list1.count())
print(list1.search(20))