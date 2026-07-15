"""
1679. Max Number of K-Sum Pairs
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.
Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

Example 2:

Input: nums = [3,1,3,4,3], k = 6
Output: 1
Explanation: Starting with nums = [3,1,3,4,3]:
- Remove the first two 3's, then nums = [1,4,3]
There are no more pairs that sum up to 6, hence a total of 1 operation.
"""
#count frequencies, then greedily match each number with its complement k - num.
"""
“A greedy algorithm builds a solution step by step, always choosing the locally optimal move at each stage, with the hope that this leads to a globally optimal solution.”
Greedy = “simple rule: take the best immediate option.”
"""

def maxOperations(self, nums: List[int], k: int) -> int:
        hashkey = {}
        counter = 0
        for i in nums:
            if i in hashkey:
                hashkey[i]+=1
            else:
                hashkey[i] = 1
        for key in list(hashkey.keys()):
            diff = k-key # no need to take abs as even if the key or element is negative , algebra wont support if abs is taken. Though with constraints in the qustion negative k or element is not allowed.
            if diff in hashkey:
                if diff == key:
                    pairs = hashkey[diff]//2
                    counter += pairs
                    hashkey[key] -=counter*2

                else:
                    pairs= min(hashkey[diff], hashkey[key])
                    counter += pairs
                    hashkey[diff] -=pairs
                    hashkey[key] -=pairs
        return counter
            

        
