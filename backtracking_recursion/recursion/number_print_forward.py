def nums_print(nums):
    if nums == 0:
        return
    nums_print(nums-1)
    print(nums)

nums_print(5)