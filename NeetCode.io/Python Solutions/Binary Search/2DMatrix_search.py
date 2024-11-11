def searchMatrix(matrix, target):
    for row in matrix:
        r = len(row) - 1
        l = 0
        if row[r] == target:
            return True
        elif row[r] < target:
            continue
        while l <= r:
            middle = l + (r - l) // 2
            if row[middle] < target:
                l = middle + 1
            elif row[middle] > target:
                r = middle - 1
            elif row[middle] == target:
                return True
    return False