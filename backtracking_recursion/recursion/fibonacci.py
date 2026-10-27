def fibonacci(n):
    if n ==1 or n==0:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

#t.c = number of calls + wd in each call(k constant)
#t.c = 2^0+ 2^1 + 2^2 + 2^3 + 2^4 its a g.p hence sum of gp = a ( r^n - 1)/(n-1) = 2^n -1  
# t.c = 2^n 
# t.c =O(2^n)
# Hence it is a really bad t.c
# Space Complexity = depth of recursion tree + memory taken in each call (k)
#                  = n + k
# space complexity = O(n)
