def findMaxConsecutiveOnes(nums) -> int:
        curr_max=0
        new_max=0
        prev_num=None
        for num in nums:
            
            if num==0:
                new_max=0
            
            if num==1 and prev_num==0:
                new_max=1
                
            if num==1 and (num==prev_num or prev_num==None):
                new_max+=1
                
            if new_max>curr_max:
                curr_max=new_max        
            print(num,prev_num,new_max)
            prev_num=num
            
            
            
        print(curr_max)

findMaxConsecutiveOnes([1,1,0,1])
            