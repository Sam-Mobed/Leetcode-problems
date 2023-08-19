"""
Just to test stuff.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hIndex(citations) -> int:
    d = {}

    h_index = 0
    for c in citations:
        if c==0:
            continue

        if c not in d:
            d[c]=1
        else:
            d[c]+=1
            if d[c]==c and c>h_index:
                h_index=c

        for key in d:
            if key>c:
                d[key]+=1
                if d[c]==c and c>h_index:
                    h_index=c

    return h_index

x=[3,0,6,1,5]
hIndex(x)