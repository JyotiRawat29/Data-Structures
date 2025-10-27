"""
201. Bitwise AND of Numbers Range
Medium
Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive.
"""
left = 5
right = 7

list1 = [i for i in range(left,right+1)]
i = 0
j = len(list1)-1
for i in range(len(list1)//2):
     result = list1[i] & list1[j]
     i += 1
     j -= 1
print(result)

