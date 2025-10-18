#%%
nums =[3,10,3]
count = 1
sum_k = 0
hm = {}
temp = nums[0]
k =1
nums.sort()
for i in range(1,len(nums)):
    diff = nums[i]-nums[i-1]
    if diff == 0:
        count+=1
    
    else:
        hm[temp] = count
        temp = nums[i]
        count = 1


hm[temp] = count

for key,v in hm.items():
    if (v%k) == 0:
        sum_k += key*v
        print(f"v is {v} sum is {sum_k}")

print(sum_k)
# %%
