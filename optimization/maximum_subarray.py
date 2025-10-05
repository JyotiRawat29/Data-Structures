"""
53. Maximum Subarray
Medium
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Intuition is: Greedy problem.
When the next element is negative, it reduces the sum, depeneding on the current sum,hence goes to restart. When positive and sum is also positive
it will continue the sum.
"""



def max_subarray(nums):
  cur=best= nums[0]
  for i in range(len(nums)):
    cur = max(nums[i]+cur, cur) # here you either extend the array or restart the array
    best = max(cur, best)
  return best
