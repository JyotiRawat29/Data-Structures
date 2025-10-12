"""
https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
169. Majority Element
Easy
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""

#%%
import math
hashmap ={}
#nums = [2,2,1,1,1,2,2]
nums = [3,2,3]
for i in range(len(nums)):
    if nums[i] in hashmap:
        hashmap[nums[i]] +=1
        if (hashmap[nums[i]] > math.floor(len(nums)/2)):
            print(nums[i])
    else:
        hashmap[nums[i]] = 1
print(nums[0]) # to handle cases when nums is a single element list like [3]
# %%
#second approach to handle single element edge case along with others
hashmap = {}
nums = [1]
for i in range(len(nums)):
    hashmap[nums[i]] = hashmap.get(nums[i],0)+1
    if hashmap[nums[i]] > len(nums)//2:
        print(nums[i])
# %%
#third approach without hashmap#count = 1
nums = [2,2,1,1,1,2,2]
candidate = nums[0]
count = 1
for i in range(1,len(nums)):
    if count == 0:
        candidate = nums[i]
    if candidate == nums[i]:
        count +=1
    else:
        count -=1
print(candidate)

# %%
