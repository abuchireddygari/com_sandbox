from tkinter import W


def sum_ranges(nums):
    res=[]
    start=nums[0]
    i=1
    
    while i < len(nums):
        if nums[i]-nums[i-1]!=1:
            if nums[i-1]!=start:
                res.append(str(start)+"->"+str(nums[i-1]))
            else:
                res.append(str(start))
            start=nums[i]
        i=i+1
    
    if nums[i-1]!=start:
        res.append(str(start)+"->"+str(nums[i-1]))
    else:
        res.append(str(start))

    return res

print(sum_ranges([0,2,3,4,6,8,9]))



