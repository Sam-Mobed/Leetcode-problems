"""
Just to test stuff.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def minWindow(s: str, t: str) -> str:

    if len(t)>len(s) or (not s) or (not t):
        return ''

    count = {}
    for char in t:
        count[char] = count.get(char,0)+1

    minlen = s
    left, right = 0, 0
    charSeen = {}
    while left<len(s):

        while right<len(s):
            char = s[right]
            charSeen[char] = charSeen.get(char, 0) + 1

            if len(s[left:right])>=len(t):
                keepGoing = False
                for c in count:
                    if (c not in charSeen) or (charSeen[c]<count[c]):
                        keepGoing = True
                        break
                
                if not keepGoing:
                    if len(s[left:right+1])<len(minlen):
                        minlen = s[left:right+1]
                    charSeen = {}
                    break
                    
                        
            right+=1

        left+=1
        right+=1
    
    return minlen


print(minWindow("ADOBECODEBANC", "ABC"))