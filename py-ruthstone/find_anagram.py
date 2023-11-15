import timeit

def is_anagram_chk(str1,str2):

    is_anagram=True

    if len(str1)!=len(str2):
        return not is_anagram

    list2=list(str2)

    idx1=0

    while idx1<len(str1) and is_anagram:
        
        idx2=0
        is_found=False
       
        while idx2<len(list2) and not is_found:
            
            if str1[idx1]==list2[idx2]:
                is_found=True
            else:
                idx2=idx2+1
        
        if is_found:
            list2[idx2]=None
        else:
            is_anagram=False
        
        idx1=idx1+1

 
    return is_anagram

def is_anagram_srt(str1,str2):

    is_anagram=True

    if len(str1)!=len(str2):
        return not is_anagram
    
    list1=list(str1)
    list2=list(str2)
    list1.sort()
    list2.sort()

    idx1=0

    while idx1<len(list1) and is_anagram:
        if list1[idx1]==list2[idx1]:
            idx1=idx1+1
        else:
            is_anagram=False
    
    return is_anagram

def is_anagram_cnt(str1,str2):
    
    is_anagram=True

    if len(str1)!=len(str2):
        return not is_anagram
    
    list1=[0]*26
    list2=[0]*26

    for i in range(len(str1)):
        pos=ord(str1[i])-ord("a")
        list1[pos]=list1[pos]+1

    for i in range(len(str2)):
        pos=ord(str2[i])-ord("a")
        list2[pos]=list2[pos]+1

    i=0
    

    while i<26 and is_anagram:
        if list1[i]==list2[i]:
            i=i+1
        else:
            is_anagram=False
    
    return is_anagram

print("--------------------")
str1="heart"
str2="earth"

print(is_anagram_chk(str1,str2))
print(is_anagram_srt(str1,str2))
print(is_anagram_cnt(str1,str2))

def test1():
    list1=[]
    for i in range(1000):
        list1=list1+[i]

def test2():
    list2=[]
    for i in range(1000):
        list2.append(i)

def test3():
    list3=[i for i in range(1000)]

def test4():
    list4=list(range(1000))

print("--------------------")

t1=timeit.Timer("test1()","from __main__ import test1")
print("concat",t1.timeit(number=10),"msec")

t2=timeit.Timer("test2()","from __main__ import test2")
print("append",t2.timeit(number=10),"msec")

t3=timeit.Timer("test3()","from __main__ import test3")
print("comprehension",t3.timeit(number=10),"msec")

t4=timeit.Timer("test4()","from __main__ import test4")
print("list range",t4.timeit(number=10),"msec")

import glob

print(glob.glob("*"))