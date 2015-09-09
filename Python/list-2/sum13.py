def sum13(nums):
    i=0
    while i < len(nums):
        if(nums[i])==13:
            nums[i]=0
            if i<len(nums)-1:
                nums[i+1]=0
        i+=1
    return sum(nums)
