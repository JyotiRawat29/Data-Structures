"""
875. Koko Eating Bananas

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.
Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""


piles = [3,6,7,11]
h = 8

high = max(piles)
low = 1

def isTrue(mid,piles):
    hours = 0
    for pile in piles:
        hours += (pile+mid-1)//mid
    return hours<=h

while(low<=high):
    mid = (low+high)//2
    if isTrue(mid,piles):
        answer = mid
        high = mid-1
    else:
        low = mid +1

print(answer)
#if hours in which koko is eating bananas is less than h, than koko need to decrease her speed and eat slowly hence mid-1.
#if hours in which kokois eating is finishing bananas is more than h, than koko needs to eat fast hence low = mid+1

#leetcode format
class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        high = max(piles)
        low = 1
        while low<=high:
            mid = (high+low)//2
            if self.ispossible(mid,piles,h):
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans

    def ispossible(self,mid,piles,h):
        hours = 0
        for pile in piles:
            hours += (pile+mid-1)//mid
        return hours<=h