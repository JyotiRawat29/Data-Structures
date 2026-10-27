def subset(arr,ans,i):
    if i==len(arr):
        return(print(ans))
    ans.append(arr[i])
    subset(arr,ans,i+1)
    ans.pop() #backtrack
    subset(arr,ans,i+1) #exclusion step

subset([1,2,3],[],0)