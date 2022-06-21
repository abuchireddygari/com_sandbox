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

class ListUnSorted:
    
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
            print(cur_node.get_data())
            cur_node=cur_node.get_next()
            
    def count(self):
        cnt=0
        if self.head==None:
            return cnt
        
        cur_node=self.head

        while cur_node!=None:
            print(cur_node.get_data())
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

    
    def replace(self,value):
        is_found=False
        cur_node=self.head
        pre_node=self.head
        while cur_node!=None and not is_found:
            #print(cur_node.get_data(),value)
            if cur_node.get_data()==value:
                if pre_node==self.head:
                    self.head=cur_node.get_next()
                else:
                    pre_node.set_next(cur_node.get_next())
                is_found=True
            else:
                pre_node=cur_node
                cur_node=cur_node.get_next()



list1=ListUnSorted()
list1.add_data(10)
list1.add_data(20)
list1.add_data(30)
list1.add_data(40)
list1.add_data(50)
list1.add_data(60)
list1.add_data(70)
print("traverse")
list1.traverse()
print("count")
print(list1.count())
print("search")
print(list1.search(20))
print("replace")
list1.replace(20)
print("traverse")
list1.traverse()
print("count")
print(list1.count())