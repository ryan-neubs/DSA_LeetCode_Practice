def threeSum(nums):
    sums = []
    for x in nums:
        for y in nums:
            for z in nums: 
                if x == y or z == y or x == z:
                    continue
                curr = sorted([x,y,z])
                print(sum(curr))
                if sum(curr) == 0 and curr not in sums:
                    sums.append(curr)
    return sums
print(threeSum([-1,0,1,2,-1,-4]))
