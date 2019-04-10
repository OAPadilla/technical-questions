# Given n non-negative integers a1, a2, ..., an , where each represents a point at
# coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
# line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
# container, such that the container contains the most water.


# O(n^2) Bruteforce Solution
def find_max_area(heights):
    max_area = 0
    for i in range(len(heights)):
        for j in range(i+1, len(heights)):
            # area = minimum x * change in y
            area = min(heights[i], heights[j]) * (j - i)
            max_area = max(max_area, area)
    return max_area()


# O(n) Two Pointer Solution
def find_max_area2(heights):
    max_area = 0
    l = 0
    r = len(heights) - 1

    while l < r:
        area = min(heights[l], heights[r]) * (l - r)
        max_area = max(max_area, area)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

print(find_max_area2([1, 8, 6, 2, 5, 4, 8, 3, 7]))
