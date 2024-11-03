# Go to website for this one. Requires diagram
# https://neetcode.io/problems/max-water-container

def maxArea(heights):
    l, r = 0, len(heights) - 1
    res = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l) # Calculate current area
        res = max(area, res) # Set result to the max between itself and curr area calc
        if heights[l] <= heights[r]: # Choose which wall to move from. Move away from shortest wall
            l += 1
        else:
            r -= 1

    return res

maxArea([1,7,2,5,4,7,3,6])