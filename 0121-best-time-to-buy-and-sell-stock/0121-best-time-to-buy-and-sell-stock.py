#class Solution:
    #def maxProfit(self, prices: List[int]) -> int:
        #maxprofit = 0
        #for i in range(len(prices)):
            #for j in range(i+1, len(prices)):
                #profit = prices[j] - prices[i]
                #if profit > maxprofit:
                   # maxprofit = profit 
        #return  maxprofit

class Solution:
    def maxProfit(self, prices: List[int]):

        min_price = prices[0]
        max_profit = 0

        for price in prices:

            if price < min_price:
                min_price = price

            profit = price - min_price

            if profit > max_profit:
                max_profit = profit

        return max_profit
