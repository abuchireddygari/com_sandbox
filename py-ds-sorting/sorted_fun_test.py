from random import randint
from timeit import repeat

def run_sorting_algorithm(algorithm,array):
    
    if algorithm!="sorted":
        setup_code = f"from __main__ import {algorithm}"
    else:
        setup_code=""

    stmt = f"{algorithm}({array})"

    times = repeat(setup=setup_code,stmt=stmt,repeat=3,number=5)
    print(times)

    print(f"Algorithm: {algorithm}. Minmum execution time: {min(times)}")

def selection_sort(array):
    n=len(array)

    for i in range(n):
        min_idx=i
        for j in range(i+1,n):
            if array[min_idx]>array[j]:
                min_idx=j
        array[i],array[min_idx]=array[min_idx],array[i]

    return array

def insertion_sort(array):
    n=len(array)

    for i in range(1,n):
        key=array[i]
        j=i-1
        while j>=0 and array[j]>key:
            array[j+1]=array[j]
            j-=1
        array[j+1] = key

    return array

def bubble_sort(array):
    n=len(array)

    for i in range(n):
        is_sorted=True
        for j in range(n-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
            
            is_sorted=False
        if is_sorted:
            break
    return array

def merge_sort(array):
    
    if len(array)<2:
        return array
    
    mid = len(array)//2

    return util_merge(l_array=merge_sort(array[:mid]),r_array=merge_sort(array[mid:]))

def util_merge(l_array,r_array):
    
    if len(l_array)==0:
        return r_array
    
    if len(r_array)==0:
        return l_array
    
    res = []

    l_index = r_index = 0

    while len(res) < len(l_array) + len(r_array):
        
        if l_array[l_index] <= r_array[r_index]:
            res.append(l_array[l_index])
            l_index+=1
        else:
            res.append(r_array[r_index])
            r_index+=1

        if l_index==len(l_array):
            res += r_array[r_index:]
            break
        if r_index==len(r_array):
            res += l_array[l_index:]
            break

    return res


ARRAY_LENGTH = 10000

if __name__=="__main__":
    array = [randint(0,1000) for i in range(ARRAY_LENGTH)]

    # print("input")
    # print(array)
    # print("output")    
    # print(merge_sort(array=array))

    print("Alogorithms:")
    print("0.built-in sorted")
    print("1.selection_sort")
    print("2.bubble_sort")
    print("3.insertion_sort")
    print("4.merge_sort")
    print("100.all")
    choice = int(input("choose a num: "))

    match choice:
        case 0:
            run_sorting_algorithm("sorted",array)
        case 1:
            run_sorting_algorithm("selection_sort",array)
        case 2:
            run_sorting_algorithm("bubble_sort",array)
        case 3:
            run_sorting_algorithm("insertion_sort",array)
        case 100:
            run_sorting_algorithm("selection_sort",array)
            run_sorting_algorithm("bubble_sort",array)
            run_sorting_algorithm("sorted",array)

