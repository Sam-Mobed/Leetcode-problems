"""
find the biggest gaps.
find the minimum, and then find the maximum.

however, once you buy once you can't buy again 
until you sell your stock.

find min, find max,
max has to come after min.
this becomes our delta.

then find min, find max again. (excluding previous max)
now check if the indices between these one is closer
if they are, it might mean that we can buy/sell another time.

so we have to build a table of max/mins with their profit 
and distance, and then see which purchases are compatible


"""

