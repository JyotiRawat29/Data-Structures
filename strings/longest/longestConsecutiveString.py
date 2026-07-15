#%%
#binary sort
        #if nums == []:
        #    return 0
        #if len(nums) == 1:
        #    return 1
        #for j in range(len(nums)):
        #    for i in range(len(nums)-1,0,-1):
        #        if nums[i] < nums[i-1]:
        #            temp = nums[i-1]
        #            nums[i-1] = nums[i]
        #            nums[i] = temp
        #        elif nums[i] - nums[i-1]  == 0:
        #            continue
        #remove duplication
        #nums = [nums[i] for i in range(len(nums)) if i == 0 or nums[i]-nums[i-1] != 0]

#%%






nums = [100,4,200,1,3,2,1]
for j in range(len(nums)):
    for i in range(len(nums)-1,0,-1):
        if nums[i] < nums[i-1]:
            temp = nums[i-1]
            nums[i-1] = nums[i]
            nums[i] = temp

#%%     
nums = list(set(nums))
#nums = [nums[i] for i in range(len(nums)) if i == 0 or nums[i] != nums[i-1]]
#%%
dict_len = {}
next_ = len(nums)-1
key = nums[next_]
counter = 1
for i in range(len(nums)-1,0,-1):
    if nums[i]- nums[i - 1] == 1:
        dict_len[key] = counter + 1
        counter += 1
        print(dict_len)
    else:
        next_ -=1
        counter = 1
        key = nums[next_]
if dict_len == {}:
            print(1)
print( max(dict_len.values()))
    
# %%
nums = [1,2,6,7,8]
nums_set = set(nums)
max_len = 0
for num in nums_set:
     if num-1 not in nums_set:
          length = 1
          while num +length in nums_set:
                length += 1
          max_len = max(max_len,length)
print(max_len)

# %%
