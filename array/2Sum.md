EASY
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

Constraint Questions:
1. Would there be an empty list? No
2. Would there be negative numbers? No

Intuition:
The difference between the target and the element should also present in the array if target < element in the array.
I need to return the index of both elements so I save index of the elements as the key to the difference of it with target.
nums = [2,7,11,15]
target = 9
Converts nums to a hashmap with their indices:
 {
 2:0,
 7:1,
 11:2,
 15:3
 }
 now 9-2 is 7 checkeck value of 7 in hash which is index of the other number.

   
