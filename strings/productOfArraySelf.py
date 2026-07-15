#%%
nums = [2,2,3,4]
prefix = 1
suffix = len(nums)-1
answer = [1]*len(nums)
for i in range(len(nums)):
    prefix = i-1
    suffix = len(nums)-i
    
    while(prefix < len(nums) and suffix > 0 and prefix <= suffix):
        if prefix < suffix:
            answer[i] = answer[i]* nums[prefix]*nums[suffix]
            prefix +=1
            suffix -=1
        elif prefix == suffix:
            answer[i] = answer[i]*nums[suffix]
            print(answer[i])
            prefix +=1

        else:
            break
print(answer)
