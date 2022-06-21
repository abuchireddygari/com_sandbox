class Stack:
    
    def __init__(self):
        self.items=[]
    
    def is_empty(self):
        return self.items==[]

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

print("-------------------------")

s=Stack()

print(s.is_empty())
print(s.size())
print(s.push(10))
print(s.push(20))
print(s.push("string"))
print(s.pop())
print(s.peek())
print(s.size())
print("-------------------------")

def rev_string(orig_str):
    
    stk=Stack()
    rev_str=""
    
    for s in orig_str:
        stk.push(s)
    
    while not stk.is_empty():
        rev_str=rev_str+stk.pop()

    return rev_str


print(rev_string("palindrome"))
print(rev_string("number"))
print("-------------------------")

def par_balance(par_str):

    is_balanced=True
    idx=0
    stk=Stack()

    while idx<len(par_str) and is_balanced:
        if par_str[idx]=="(":
            stk.push("(")
        else:
            if stk.is_empty():
                is_balanced=False
            else:
                stk.pop()
        idx=idx+1

    if is_balanced and stk.is_empty():
        return is_balanced
    else:
        return not is_balanced

print(par_balance("((()))"))
print(par_balance("(()((())()))"))
print(par_balance("(()()(()"))
print("-------------------------")

def sym_balance(sym_str):
    is_balanced=True
    idx=0
    stk=Stack()

    while idx<len(sym_str) and is_balanced:
        if sym_str[idx] in "([{":
            stk.push(sym_str[idx])
        else:
            if stk.is_empty():
                is_balanced=False
            else:
                if not sym_match(stk.pop(),sym_str[idx]):
                    is_balanced=False
        idx=idx+1

    if is_balanced and stk.is_empty:
        return is_balanced
    else:
        return not is_balanced

def sym_match(open_sym,close_sym):
    open_seq="([{"
    close_seq=")]}"
    return open_seq.index(open_sym)==close_seq.index(close_seq)

print(sym_balance('{({([][])}())}'))
print(sym_balance('[{()]'))

print("-------------------------")


def dec_to_bin(dec_num):
    s=Stack()
    bin_str=""
    while dec_num>0:
        rem=dec_num%2
        s.push(rem)
        dec_num=dec_num//2
    
    while not s.is_empty():
        bin_str=bin_str+str(s.pop())
    
    return bin_str

print(dec_to_bin(32))
print("------------------------")
print("ABCDEFGHIJKLMNOPQRSTUVWXYZ".split())
