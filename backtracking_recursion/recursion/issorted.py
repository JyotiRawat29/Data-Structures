def issorted(arr,size):
    if size==0 or size==1:
        return True
    if arr[size-1]>=arr[size-2] and issorted(arr,size-1):
        return True



print(issorted([1,2,3,4,5],5))

#T.C = O(n)
#S.C = O(n)