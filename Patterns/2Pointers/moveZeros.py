"""
283. Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:
Input: nums = [0]
Output: [0]
"""
#the approach here is to start 2 pointers from end,
#one pointer tracks the index of next zero and other scans the 0 in array.
# once 0 is found, move all the element one by one to left and decrease the counter pointer and place 0 there.
#at every 0 in array reset the scan pointer to the current element of the array
# the approach is o(n^2) for worst case 
def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_counter = len(nums) -1
        read = len(nums) -1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == 0:
                read = i
                while(read<zero_counter):
                    nums[read]=nums[read+1]
                    read+=1
                nums[zero_counter] = 0
                zero_counter -=1
        return nums

#t.c is o(n^2) fo worst case while s.c is O(1)

#Optimize solution
#fast and slow pointer
#the approach is to squeeze all the non zero to the right and at the end fill the remaining array elements with 0
def moveZeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
    for i in range(slow, len(nums)):
        nums[i] = 0
    return nums
#T.C O(n) and s.c O(1)

