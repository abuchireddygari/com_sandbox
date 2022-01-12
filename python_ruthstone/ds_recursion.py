
def list_sum(list1):
    sum=0
    for i in list1:
        sum=sum+i
    return sum

def rec_sum(list1):
    if len(list1)==1:
        return list1[0]
    return list1[0]+rec_sum(list1[1:])

def num_to_basestr(num,base):
    look_up_str="0123456789ABCDEF"
    if num<base:
        return look_up_str[num]
    return num_to_basestr(num//base,base)+look_up_str[num%base]

def rec_str_rev(in_str):
    if len(in_str)==1:
        return in_str[0]
    return rec_str_rev(in_str[1:])+in_str[0]


list1=[1,3,5,7,9]
print("for loop sum")
print(list_sum(list1))
print("recursion sum")
print(rec_sum(list1))
print("recursion number to base string")
print(num_to_basestr(10,2))
print("recursion reverse string")
print(rec_str_rev("ashok"))