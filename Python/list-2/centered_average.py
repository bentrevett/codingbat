def centered_average(nums):
    nums.remove(max(nums))
    nums.remove(min(nums))
    total=0
    for i in range(len(nums)):
        total+=nums[i]
    average=total/len(nums)
    return average
