def subset(arr,ans,i):
    if i==len(arr):
        return(print(ans))
    ans.append(arr[i])
    subset(arr,ans,i+1)
    ans.pop() #backtrack
    subset(arr,ans,i+1) #exclusion step

subset([1,2,3],[],0)

#T.c = 2^n * n * wd (o(1)) = (2^n)*n
#s.c= 2^n though we are not saving the subsets and just saving hence s.c = 1
