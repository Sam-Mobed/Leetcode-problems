"""
Just to test stuff.
"""

def combine(n: int, k: int):

    res = []

    def backtrack(num,currList):
        if num>n:
            res.append(currList[:])
            return
        if len(currList)==k:
            res.append(currList[:])
            backtrack(num,currList[:(k-1)])
            return
        backtrack(num+1,currList+[num])
    
    for i in range(1,n):
        backtrack(i,[])

    if n==1:
        return [[1]]
    return res

print(combine(4,2))