#input n, output = 1+2+3+4+......+n

def sum_nums(nums):
    if nums == 1:
        return 1
    return nums + sum_nums(nums-1)

print(sum_nums(5))

#time complexity = number of recursion calls + work done in each call
#                = O(n)+k
#                = O(n)

#Space Complexity = height of recursion tree + memory taken in each call
#                 = O(n)+ O(1)
#                 = O(n)