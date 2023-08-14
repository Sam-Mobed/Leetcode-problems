"""
Just to test stuff.
"""

def minSubArrayLen(target, nums) -> int:
    minlen=float('inf')

    l,r=0,1

    while l<len(nums):
        s = sum(nums[l:r])
        if s<target:
            r+=1
        elif s>target:
            l+=1
            r=l+1
        elif s==target:
            minlen = min(minlen,len(nums[l:r]))
            l+=1
            r=l+1
    
    if minlen==float('inf'):
        return 0
    return minlen

minSubArrayLen(7,[2,3,1,2,4,3])