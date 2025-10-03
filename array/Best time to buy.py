#https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_value = float('inf')
        best_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_value:
                min_value = prices[i]
            else:
                best_profit = max(best_profit, prices[i]-min_value)
        
        return best_profit
        
