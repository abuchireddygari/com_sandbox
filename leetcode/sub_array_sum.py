def sub_arr_sum(nums,k):
    curr_sum=0
    cnt=0
    hash_map={}
    for num in nums:
        curr_sum=curr_sum+num
        
        if curr_sum==k:
            cnt=cnt+1
        
        if curr_sum-k in hash_map:
            cnt=cnt+hash_map[curr_sum-k]
        
        if curr_sum in hash_map:
            hash_map[curr_sum]=hash_map[curr_sum]+1

        else:
            hash_map[curr_sum]=1

    return cnt

lists=[1,1,1,2,2,1]

print(sub_arr_sum(lists,2))
for i in range(1,len(lists),2):
    print(i)