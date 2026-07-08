"""
Increasing Triplet Subsequence
Given an integer array nums, return true if there exists a triple of indices 
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: One of the valid triplet is (1, 4, 5), because nums[1] == 1 < nums[4] == 4 < nums[5] == 6.

"""
#Solution Brute Force
#Bruteforce approach to find increasing triplet in an array
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        for num in range(len(nums)-2):
            for start in range(num + 1, len(nums)-1):
                end = start+1
                while(end != len(nums)):
                    if nums[num]<nums[start]:
                        while(end!=len(nums)):
                            if nums[start]<nums[end]:
                                return True
                            else:
                                end += 1
                    else:
                        start += 1
                        end = start + 1
        return False

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    s = Solution()
    print(s.increasingTriplet(nums))

"""
If we find 2 smallest numbers in the array, then we can check if there is any number greater than the second smallest number. 
If yes, then we have found an increasing triplet.
To build that concept, first try to build on finding smallest number in the array.
Then we can build on that to find second smallest number and 
then finding third greatest number in array.

In the question we just need to find if there is any increasing triplet in the array,
so we can just return True if we find any number greater than second smallest number, no need to 
find the actual triplet (hence saving time and space complexity)

"""

"""
# algorithm to find three smallest numbers in the aray
first = float('inf')
second = float('inf')
third = float('inf')

nums = [1,5,0,4,1,3]
for num in nums:
    if num <=first:
        third = second
        second = first
        first = num
    elif num <= second:
        third = second
        second = num
    elif num <= third:
        third = num
print(first, second, third)

"""

#Optimize solution
#Trick is to find the two smallest number, if there exist any number greater than second smallest number than we have found the indices.

first = float('inf')
second = float('inf')

for num in nums:
    if num <= first:
        first = num
    elif num <= second:
        second = num
    else:
        print("Found increasing triplet")
        #Here at any point in thr loop first < second
        #Both are already found hence we just to check if there is any number greater than second smallest number
        #which is num>second: else is covering that case becasue if num > second, it is also greater than first
        #hence we can just return True if we find any number greater than second smallest number, no need to 
        #find the actual triplet (hence saving time and space complexity)
        break
