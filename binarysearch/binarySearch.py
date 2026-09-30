#704. Binary Searc
"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1

Constraints:

    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.

"""

nums, target = [-1,0,3,5,9,12], 9
nums.sort()

low = 0
high = len(nums)-1
while(low<=high):
    mid = (low+high)//2

    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]>target:
        high=mid-1
    else:
        low=mid+1
else:#belongs to while loop, if no break occurs
    print(-1)

#LEET CODE
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = -1
        while(low<=high):
            mid = (low+high)//2
            if target < nums[mid]:
                high = mid-1
            elif target > nums[mid]:
                low = mid+1
            else:
                ans = mid
                return ans
        return -1
    
