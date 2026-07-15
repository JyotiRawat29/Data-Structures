class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        max_candies = max(candies)
        result = [c + extraCandies >= max_candies for c in candies]
        return result

if __name__ == "__main__":
    candies = [2,3,5,1,3]
    extraCandies = 3
    s = Solution()
    print(s.kidsWithCandies(candies, extraCandies))

"""
The solution runs in O(N) time and O(n) space, which is optimal since we must evaluate every child.”
O(n) S.C comes from required output and not auxiliary space. The solution is simple and efficient, 
using a list comprehension to generate the result in a single line.
"""