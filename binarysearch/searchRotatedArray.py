#33. Search in Rotated Sorted Array
"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Constraints:
1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104


"""
# 1. Calculate the mid and check if it is target index.
# 2. Now check the left side and right side of array and find which side is sorted. In rotated array, there is alwys one side which is sorted. Thats the property of rotated array.
# 3. If left Array is sorted, check if the target value lie within the range or not. If it lies than apply BS there i.e. check arr[low]<=target<=arr[mid] and make high = mid-1,limiting the search space.
# 4. If left Array is not sorted that means right array is sorted, hence apply BS there i.e. check arr[mid]<=target<=arr[high], if it lies low = mid+1, if not high = mid-1



class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = -1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]== target:
                ans = mid
                return ans
            if nums[low]<=nums[mid]: 
                #left array is sorted
                #apply Binary Sort in sorted array
                if nums[low]<=target and target<=nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else: 
                #Right array is sorted
                if nums[mid]<=target and target<=nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return ans
