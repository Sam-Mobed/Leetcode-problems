"""
Just to test stuff.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def permute(nums):

    result = []

    if len(nums)==1:
        return [nums[:]]
    
    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)
    
    return result


permute([1,2,3])