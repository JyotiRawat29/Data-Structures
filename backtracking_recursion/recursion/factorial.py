def facto(nums):
    if nums ==1:
        return 1
    return nums*facto(nums-1)

print(facto(5))

#Time complexity = #recursion calls + work done in each call 
#                = n + constant
#                = o(n)+ k = O(n)
# 
# Space complexity = height of recursion tree + memory taken in each call
#                   = n + k
#                   = O(n)     