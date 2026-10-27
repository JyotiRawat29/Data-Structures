# 1. Sort the array
# 2. Find the subsets

def subsets_dupli(arr,ans,counter):
    arr.sort()  #sorting is necessary for this approach
    if counter==len(arr):
        res.append(ans.copy())
        return
    ans.append(arr[counter])
    subsets_dupli(arr,ans,counter+1)
    ans.pop()
    idx=counter+1
    while(idx<len(arr) and arr[idx]==arr[idx-1]):
        idx+=1
    subsets_dupli(arr,ans,idx)

res = []
subsets_dupli([1,2,2],[],0)
print(res)

