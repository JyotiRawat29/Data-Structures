def subsets(arr,ans,counter,res):
    if counter == len(arr):
        res.append(ans.copy())
        return
    ans.append(arr[counter])
    subsets(arr,ans,counter+1,res)
    ans.pop()
    subsets(arr,ans,counter+1,res)

res = []
print(subsets([1,2,3],[],0,res)) #will return None as subsets function is returning None its the res variable that is tsoring the subsets, hence
print(res)

#in leetcode style
def subsets(arr):
    res = []

    def subsets(ans,counter):
        if counter == len(arr):
            res.append(ans.copy())
            return
        ans.append(arr[counter])
        subsets(ans,counter+1)
        ans.pop()
        subsets(ans,counter+1)
    subsets([],0)
    return res
print(len(subsets([1,2,3,10])))
print(subsets([1,2,3,10]))

#T.c= n*O(2^n)
#S.c = O(2^n)