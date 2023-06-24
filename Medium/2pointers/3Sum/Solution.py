#you can't pop elements to avoid duplicates, one element can
#be included in multiplee triplets

#if nums size less than 3 return [],
#if it is three do sum(nums) to check
#elements inside triplet must be distinct

"""
what if wwe sort the array, then try smallest elements
with biggest, and theen middle elements together
-the logic is that middle elements won't be big/small
 enough for extreme values
-not sure if you can do this unless it is bruteforce or :
- if you look at the solution, you have three possibilities:
    (neg,pos,pos),(neg,neg,pos), (neg, zero, pos) (or 0,0,0)
    you need to have this format or else values will not cancel each
    other out.
    also, values can't be repeated.
    thinking of it this way, we don't need to bruteforce it
triangle inequality: any two sides are bigger than the other one
"""

#choose a negative, choose a positive

def threeSum(nums):
    #not sure if these are necessary
    if (len(nums)<3):
        return []
    elif (len(nums)==3 and sum(nums)!=0):
        return []
    elif (len(nums)==3):
        return nums
    
    triplets=[]

    

    return triplets
