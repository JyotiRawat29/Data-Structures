"""
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

"""

nums, target = [1,3,5,6], 2
def searchInsert(nums: list[int], target: int) -> int:
    low = 0
    high = len(nums)-1
    while(low<=high):
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            low = mid+1
        else:
            high = mid-1
    #if target>nums[mid]: #this fails because[1,3,5,6] target = 0, here num[0]=1 hence mid-1 -1 hence we recieve output 1 but it should be 0
    #    return mid+1
    #else:
    return low # still confused about why low
print(searchInsert(nums,target))