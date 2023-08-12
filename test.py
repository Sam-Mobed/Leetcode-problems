"""
Just to test stuff.
"""

def maxProfit(prices) -> int:

    buy=0
    sell=0
    gain = prices[sell]-prices[buy]

    for i in range(len(prices)):
        if prices[i]<prices[buy] and prices[sell]-prices[i]<=gain:
            buy=i
            sell=i
        elif prices[i]>prices[sell]:
            sell=i
        gain=prices[sell]-prices[buy]

    return gain

maxProfit([2,1,2,1,0,1,2])