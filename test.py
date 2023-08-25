"""
Just to test stuff.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def insert(trie,word):
    for i,c in enumerate(word):
        if c in trie:
            if trie[c][1] or i==len(word)-1:
                return True
        else:
            trie[c] = {}, i==len(word)-1
            
        trie,_ = trie[c]
    return False

def noPrefix(words):
    trie = {}
    for word in words:
        if insert(trie,word):
            print("BAD SET")
            print(word)
            return
    print(trie)
    print("GOOD SET")


noPrefix(['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad'])
