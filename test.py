"""
Just to test stuff.
"""

def candy(ratings) -> int:
        
    candies=[1]*len(ratings)
        
    for i in range(0,len(ratings)-1):
        if ratings[i+1]>ratings[i] and candies[i+1]<=candies[i]:
            candies[i+1]+=1

    for i in range(len(ratings)-1,0,-1):
        if ratings[i-1]>ratings[i] and candies[i-1]<=candies[i]:
            candies[i-1]+=1

    return sum(candies)

candy([1,2,87,87,87,2,1])