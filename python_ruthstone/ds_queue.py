class Queue:
    
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

print("--------------------------------")

q = Queue()

print(q.is_empty())
print(q.size())
print(q.enqueue(8.4))
print(q.dequeue())
print(q.enqueue(True))
print(q.enqueue(10))
print(q.is_empty())
print(q.size())

print("--------------------------------------")

def hot_potato(name_list,num):
    
    q=Queue()
    
    for n in name_list:
        q.enqueue(n)
    
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        print(q.dequeue())
    
    return q.dequeue()

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7))

print("-----------------------------------")

class Deque:
    
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]
    
    def size(self):
        return len(self.items)
    
    def add_front(self,item):
        self.items.append(item)
    
    def add_rear(self,item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()
    
    def remove_rear(self):
        return self.items.pop(0)

def is_palindrome(st):
    is_pal=True
    dq=Deque()
    for c in st:
        dq.add_rear(c)
    while dq.size()>1 and is_pal:
        if dq.remove_front()!=dq.remove_rear():
            is_pal=False
    return is_pal

print("-----------------------------------")
print(is_palindrome("lsdkjfskf"))
print(is_palindrome("radar"))
print(is_palindrome("malayalam"))
print(is_palindrome("101101"))
print(is_palindrome("1011011"))

print("-----------------------------------")