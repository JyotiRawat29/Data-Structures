"""
70. Climbing Stairs

Easy

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
 
"""

import math
def climbStairs(n: int) -> int:
    total_num_of_ways = 1
    least_number_of_steps= math.ceil(n/2)
    for index,i in enumerate(range(int(least_number_of_steps),n)):
        count_of_2s = math.floor(n/2)-index
        count_of_1s = n - 2 * (count_of_2s)
        X = min(count_of_2s,count_of_1s)
        temp = 1
        if X!=0:
            k=i
            for j in range(X):
                temp *=k
                k-=1
            temp = int(temp/math.factorial(X))
        total_num_of_ways+=temp
    return total_num_of_ways

climbStairs(5)