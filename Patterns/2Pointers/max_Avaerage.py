"""
643. Maximum Average Subarray I

You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

Example 1:
Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:
Input: nums = [5], k = 1
Output: 5.00000

"""

#%%
nums = [0,4,0,3,2]
k = 2
sum0 = 0
for i in range(k):
    sum0+=nums[i]
max_sum = sum0
print(sum0)
right = k
left = 0
while(right<len(nums)):

    sum0= sum0 - nums[left] + nums[right]
    max_sum = max(sum0, max_sum) 
    print("sum0",sum0)
    right +=1
    left +=1

    
print(sum0/k) 
