"""
Aggressive Cows
#GFG problem
Given an integer array arr[], which denotes the positions of stalls. All the positions are distinct. There are k aggressive cows.
Assign the cows to the stalls such that the minimum distance between any two cows is maximized.
Input: arr[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at arr[0], the second at arr[2], and the third at arr[3]. The minimum distance between any two cows is 3 (between arr[0] and arr[2]), which is the maximum possible among all valid arrangements.

https://www.youtube.com/watch?v=7wOzDqsfXy0
"""

arr,k = [1, 2, 4, 8, 9], 3
def checkTrue(mid, arr, k):
    
    cows = 1
    laststallPos = arr[0]
    for a in range(1,len(arr)):
        if (arr[a]-laststallPos) >=mid: #mid is the minimum possible value, if mid could be a minimum possible value, means a cow can be placed there hence cow+1
            cows +=1
            laststallPos = arr[a]
            if cows == k: # or you keep this condition outside outer if , it is same
                return True
    return False

def aggresiveCows(arr,k):
    #sort the array
    arr.sort()
    low = 1
    high = max(arr)-min(arr)

    while(low<=high):
        mid = (low+high)//2

        if checkTrue(mid,arr,k):
            ans = mid
            low = mid+1
            #high = mid-1
        else:
            
            high = mid-1
    return ans

#%%

print(aggresiveCows(arr,k))
# %%

#GFG solution#
class Solution:
    def checkTrue(self,mid, arr, k):
        cows = 1
        laststallPos = arr[0]
        for a in range(1,len(arr)):
            if (arr[a]-laststallPos) >=mid:
                cows +=1
                laststallPos = arr[a]

            if cows == k:
                return True
        return False
        
    def aggressiveCows(self, arr, k):
        # code here
        
        arr.sort()
        low = 1
        high = max(arr) - min(arr)
        while(low<=high):
            mid = (low+high)//2
            if self.checkTrue(mid,arr,k):
                ans = mid
                #high = mid-1
                low = mid+1
            else:
                #low = mid+1
                high = mid-1
        return ans