#410. Split Array Largest Sum
"""
Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array.

Input: nums = [7,2,5,10,8], k = 2
Output: 18

Input: nums = [1,2,3,4,5], k = 2
Output: 9

"""
nums,k = [7,2,5,10,8], 2

nums,k = [1,2,3,4,5],2
def checkTrue(mid,nums,k):
    part = 1
    running_sum = 0

    for num in nums:
        if running_sum+num >mid:
            part +=1
            running_sum=num
            if part>k:
                return False
        else:
            running_sum +=num
    return True
    

def splitarraysum(nums,k):
    low = max(nums)
    high = sum(nums)

    while(low<=high):
        mid = (low+high)//2

        if checkTrue(mid,nums,k):
            ans = mid
            high = mid-1

        else:
            low = mid+1
    return ans
print(
splitarraysum(nums,k))

#leeetcode
class Solution:
    def checkTrue(self,mid, nums, k):
        part=1
        running_sum = 0
        for num in nums:
            if running_sum+num>mid:
                part+=1
                running_sum = num
                if part>k:
                    return False
            else:
                running_sum += num
        return True

    def splitArray(self, nums: list[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = (low+high)//2
            if self.checkTrue(mid, nums,k):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans
            