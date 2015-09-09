def has22(nums):
    for i in range(len(nums)):
        if nums[i]==2 and i<len(nums)-1:
            if nums[i+1]==2:
                return True
    return False
