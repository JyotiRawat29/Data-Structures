"""
11. Container With Most Water

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

"""

class Solution:
    def maxArea(self, height: list[int]) -> int:
        right = len(height) -1
        left = 0
        max_area = 0
        while(left<right):
            base = right - left
            depth = min(height[left], height[right])
            area = base * depth
            max_area = max(area,max_area)
            if height[left]<height[right]:
                left+=1
            else:
                right -=1

        return max_area

"""
the portion  
if height[left]<height[right]:
                left+=1
            else:
                right -=1
handles the comparisoon of the height from one end to each element only if the height is smaller than 
the other end because the area is limited by the smaller height and we need to find the maximum area 
hence we need to move the pointer of the smaller height to find a larger height which can give us a 
larger area.
"""
