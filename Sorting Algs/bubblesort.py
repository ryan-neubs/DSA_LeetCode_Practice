def bubblesort(nums):
    start = 0
    end = len(nums) - 1
    while end != start:
        i = 0
        j = i + 1
        while i != end:
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        end -= 1
        print(nums)

    
# [1,4,8,7,6,2,3,10,5,9]