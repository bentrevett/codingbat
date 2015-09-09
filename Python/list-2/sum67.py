def sum67(nums):
    total=0
    for i in range(len(nums)):
        if nums[i]==6:
            while 1==1:
                if nums[i]==7:
                    nums[i]=0
                    break
                nums[i]=0
                i+=1
    return sum(nums)
