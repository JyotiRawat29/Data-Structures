"""
540. Single Element in a Sorted Array

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

The even poistion always takes first element of the pair and odd position takes second element of the pair.
Hence we can use this property to find the single element in the array.
If we find that mid is even and mid+1 is equal to mid, then we can say that the single element lies on right side of mid, hence low = mid+1. 
If mid is odd and mid-1 is equal to mid, then we can say that the single element lies on right side of mid, hence low = mid+1.
If both conditions are false, then we can say that the single element lies on left side of mid, hence high = mid-1.
"""

class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:

        low = 0
        high = len(nums) - 1
        while(low<=high):
            mid = low + ((high-low)//2)
            if (mid%2==0 and nums[mid+1]==nums[mid]) or (mid%2==1 and nums[mid-1]==nums[mid]):
                low = mid+1
            else:
                high = mid-1
        return nums[low]