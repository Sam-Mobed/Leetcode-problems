"""
Just to test stuff.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def combine(inorder, postorder):

    if not inorder or not postorder:
        return None

    root = TreeNode(postorder[-1])
    mid = inorder.index(postorder[-1])
    right = postorder.index(inorder[mid+1])
    root.left = combine(inorder[:mid], postorder[:right])
    root.right = combine(inorder[mid+1:], postorder[right:-1])

    return root

print(combine([9,3,15,20,7],[9,15,7,20,3]))