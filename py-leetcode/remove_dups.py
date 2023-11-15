def remove_val(nums, val):
    idx=0
    for n in nums:
        if n!=val:
            nums[idx]=n
            idx=idx+1
    print(nums)
    return idx
print(remove_val([0,1,2,2,3,0,4,2],2))