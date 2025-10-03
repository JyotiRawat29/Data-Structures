"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/description/
Easy
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

def containsDuplicate(self, nums):
  map = {}
  for i in range(len(nums)):
    if nums[i] in map:
      return True
    map[nums[i]] = 1
  return False

"""
Do not be confused to assign the map[nums[i]] = 1 and than if condition. As it always gonna be true.
for i in range(len(nums)):
    map[nums[i]] = 1 
    if nums[i] in map: # this will always be true as in above line you are assigning it. Do not think that we need to assign hashmap first. The first clue is to check if the element is present in hashmap or not. If it is empty than assign the value, so that when the duplicate value appears it can use the previous update.
      return True
  return False
Also you do not need to initiate the counter in hash map for the element as the question only wants you to return the True or False and not how much time duplicate value appeared. So, it is unnecessary.
  """
