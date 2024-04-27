'''
You are given an array prices where prices[i] 
is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock 
and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. 
If you cannot achieve any profit, return 0

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
from typing import List


def maxProfit(prices: List[int]) -> int:
    '''
    Use sliding window, with 2 pointers
    buy pt - b and sell pt - s

    keep checking for the difference between the value of s and b
    if b > s, calculate the difference and compare with current
    profit value,
    get the max of the 2 and store as the profit
    if the b < s:
    place the sell pointer on the buy position

    increment the position of the buy pointer

    return the final profit value
    '''
    b, s = 0, 1
    profit = 0

    while s < len(prices):
        if prices[s] > prices[b]:
            diff = prices[s] - prices[b]
            profit = max(profit, diff)
        else:
            b = s

        s = s + 1

    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
