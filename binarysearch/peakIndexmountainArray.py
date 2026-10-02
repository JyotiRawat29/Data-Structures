"""
852. Peak Index in a Mountain Array

You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.

Return the index of the peak element.

Your task is to solve it in O(log(n)) time complexity.

Example 1:

Input: arr = [0,1,0]

Output: 1

Example 2:

Input: arr = [0,2,1,0]

Output: 1

Example 3:

Input: arr = [0,10,5,2]

Output: 1

"""

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:

        low =0
        high = len(arr)-1
        while(low<=high):
            mid = low + ((high-low)//2)
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]<arr[mid+1]: # increasing slope : left
                low = mid+1
            else: #decreasing slop : right
                high = mid-1
        return low
#This quetion is similar to find peak element, but here we are given that the array is mountain array hence only one peak element is present and it is not possible that the first or last element is a peak element hence we don't have to check for first and last element.
# In find peak element we check mid-1 and mid+1 because we are not given that the array is mountain array hence we have to check both sides of mid.
#In find peak element, there are multiple peaks, hence the first or last element can also be a peak therefore we have put a condition to check it.