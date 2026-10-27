def nums_print(n):
    if n==0:
        return
    print(n)
    return nums_print(n-1)

nums_print(5)

