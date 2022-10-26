nums = [1,2,3,3,3,3,5]
k = 1

for next in range(1,len(nums)):
    if nums[next] != nums[next-1]:
        nums[k] = nums[next]
        k += 1
print(k)


