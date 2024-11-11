def search(nums, target):
    l = 0
    r = len(nums) - 1
    middle = 0
    while l <= r:
        middle = l + (r - l) // 2
        # Using (l + r) // 2 can lead to integer overflow.
        # While it doesn't really happen in python it's best to practice this way

        if nums[middle] > target:
            r = middle - 1

        elif nums[middle] < target:
            l = middle + 1

        elif nums[middle] == target:
            return middle

    return -1

