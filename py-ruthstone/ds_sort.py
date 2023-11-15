def sort_bubble(i_list):
    cnt=0
    for o in range(len(i_list)-1,0,-1):
        for i in range(o):
            cnt=cnt+1
            if i_list[i]>i_list[i+1]:
                temp=i_list[i]
                i_list[i]=i_list[i+1]
                i_list[i+1]=temp
    print("bubble sort cnt",cnt)

def sort_short_bubble(ii_list):
    cnt=0
    is_exchange=True
    o=len(ii_list)-1
    while o>0 and is_exchange:
        is_exchange=False
        for i in range(o):
            cnt=cnt+1
            if ii_list[i]>ii_list[i+1]:
                is_exchange=True
                temp=ii_list[i]
                ii_list[i]=ii_list[i+1]
                ii_list[i+1]=temp
        o=o-1
    print("buble sort short cnt",cnt)

def sort_selection(iii_list):
    cnt=0
    for o in range(len(iii_list)-1,0,-1):
        max_pos=0
        for i in range(1,o+1):
            cnt=cnt+1
            if iii_list[i]>iii_list[max_pos]:
                max_pos=i
        temp=iii_list[o]
        iii_list[o]=iii_list[max_pos]
        iii_list[max_pos]=temp
        print("selection sort cnt",cnt)

def sort_insertion(iv_list):
    cnt=0
    for o in range(1,len(iv_list)):
        curr_val=iv_list[o]
        pos=o
        while pos>0 and iv_list[pos-1]>curr_val:
            cnt=cnt+1
            iv_list[pos]=iv_list[pos-1]
            pos=pos-1
        iv_list[pos]=curr_val
    print("insertion sort cnt",cnt)

def sort_merge(v_list):
    if len(v_list)>1:
        mid=len(v_list)//2
        left_half=v_list[:mid]
        right_half=v_list[mid:]
        sort_merge(left_half)
        sort_merge(right_half)

        i=j=k=0

        while i<len(left_half) and j<len(right_half):
            if left_half[i]<right_half[j]:
                v_list[k]=left_half[i]
                i=i+1
            else:
                v_list[k]=right_half[j]
                j=j+1
            k=k+1

        while i<len(left_half):
            v_list[k]=left_half[i]
            i=i+1
            k=k+1

        while j<len(right_half):
            v_list[k]=right_half[j]
            j=j+1
            k=k+1
        


i_list=[20,30,40,90,50,60,70,80,100,110]
sort_bubble(i_list)
print("buble sort:",i_list)

ii_list=[20,30,40,90,50,60,70,80,100,110]
sort_short_bubble(ii_list)
print("buble short sort",ii_list)

iii_list=[20,30,40,90,50,60,70,80,100,110]
sort_selection(iii_list)
print("selection sort",iii_list)

iv_list=[20,30,40,90,50,60,70,80,100,110]
sort_insertion(iv_list)
print("selection sort",iv_list)

v_list=[20,30,40,90,50,60,70,80,100,110]
sort_merge(v_list)
print("merge sort",v_list)


