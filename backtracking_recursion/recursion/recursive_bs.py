def binary_search(arr,target,start,end):
    if start<=end:
        
        mid = (start+end)//2
        if arr[mid]==target:
            return mid
        if arr[mid]<=target:
            return binary_search(arr,target,mid+1,end)
        else:
            return binary_search(arr,target,start,mid-1)
    return -1 #return -1 in case start>end, which happens only when target does lies in array

print(binary_search([1,3,5,6,9,11],50,0,len([1,3,5,6,9,11])-1))

#here we have written the logic using recursion, in place of how we learnt before using while (./../binarysearch/binarysearch.py)

# T.C = O(log(n))
# f(6)-->f(3)-->f(1) if size of arr is 6 than later size of arr becoming (6/2) --> (3/2)
# f(6)-->f(6/2)-->f(6/4)
# f(6/2^0)-->f(6/2^1)-->f(6/2^2)
# but here we do not know the height of recursion tree, hence lets say it is k
# f(n/2^k)--> n/(2^k)=1 --> Thats our equation --> n = 2^k --> taking log both sides --> log(n) = log(2^k) --> log(n) (base2) = k
# hence the height of recursion tree is k = log(n) we ignore the base here.
# T.C = O(log(n)) * WD in each call(o(1)) = O(log(n))
# S.C = height of recursive tree = O(log(n)) * memory taken in each call (o(1)) =   O(log(n))