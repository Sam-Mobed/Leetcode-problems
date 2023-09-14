"""
Just to test stuff.
"""

def maxOperations(nums,k) -> int:

    c = Counter(nums) # Counter({1: 1, 2: 1, 3: 1, 4: 1})
    res = 0
    seen = set()

    for x in c:
        if x not in seen and (k-x) in c:
            if x==k-x:
                res += c[x]//2
            else:
                res += min(c[x],c[k-x])
            seen.add(x)
            seen.add(k-x)

    return res

maxOperations([3,1,3,4,3],6)