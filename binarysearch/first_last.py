"""
34. Find First and Last Position of Element in Sorted Array

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Input: nums = [], target = 0
Output: [-1,-1]

"""
#Bruteforce O(n)
nums, target = [5,7,7,8,8,10], 7
start,last = -1,-1
for i in range(len(nums)):
    if nums[i]==target:
        start=i
        break
for i in range(len(nums)):
    if nums [i]==target:
        last=i
print([start,last])

#hence for optimize approach we can write two binary search functions one for first and other for last
#or we can use a switch to combine bith in one function


nums, target = [5,7,7,8,8,10], 8

def binary(nums,target,isTrue):
    low = 0 
    high = len(nums)-1
    ans = -1
    while(low<=high):
        mid = (low+high)//2

        if nums[mid]>target:
            high = mid-1
        elif nums[mid]<target:
            low = mid+1
        else:
            ans = mid
            if isTrue:
                high = mid-1
            else:
                low = mid+1
    return ans

def binaryfunct(nums,target):
    return [binary(nums,target,True),binary(nums,target,False)]

print(binaryfunct(nums,target))
##################LEETCODE with 2 functions:
def searchRange(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    first = self.findfirst(nums, target)
    last = self.findlast(nums, target)
    return [first, last]

def findfirst(self, nums, target):
    i = 0
    while(i<len(nums)):
        if nums[i]==target:
            return i
        else:
            i+=1
    return -1

def findlast(self, nums, target):
    i=len(nums)-1
    while(i>=0):
        if nums[i]==target:
            return i
        else:
            i-=1
    return -1

######LEETCODE WITH SWITCH FUNCTION#####################
class Solution:
    def binary_search(self,nums,target,isTrue):
        low = 0
        high = len(nums)-1
        ans = -1
        while(low<=high):
            mid = (low+high)//2
            if nums[mid]<target:
                low = mid+1
            elif nums[mid]>target:
                high = mid-1
            else:
                ans = mid
                if isTrue:
                    high = mid-1
                else:
                    low = mid+1
        return ans
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return([self.binary_search(nums,target,True), self.binary_search(nums,target,False)])
        

