class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price=prices[0]
        max_profit=0
        for i in range (1, len(prices)):
                if min_price>prices[i]:
                    min_price=prices[i]
                    print(min_price)
                curr_price=prices[i]
               
                if curr_price-min_price>max_profit:
                    max_profit=curr_price-min_price
        return max_profit