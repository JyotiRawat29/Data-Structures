"""
https://leetcode.com/problems/product-of-array-except-self/
MEDIUM
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
****
Intuition:
We divide it into parts: 
1. First multiply the elements that appear before the designated number :: PREFIX:: update from left
2. Multiply the elements that appear afterwards the designated element ::SUFFIX:: update from right
First you update ans using prestore value(variable suffix or prefix) and than update that variable with the current value.
prefix and suffix store the product of values before and after the elements. 
"""

def productofarray(nums):
  ans = [1] * len(nums)
  prefix = 1
  for i in range(len(nums)):
    ans[i] = prefix # ans[i]*=prefix, doesnot make a difference as the initial value in ans is 1
    prefix *=nums[i]

  suffix = 1
  for i in range(len(nums)-1, -1, -1):
    ans[i]*= suffix
    suffix*= nums[i]
    
  return ans
  
