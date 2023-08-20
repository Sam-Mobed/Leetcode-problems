"""
Just to test stuff.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def findSubstring(s: str, words):

    if len(s)==0 or (not s) or (not words):
        return []
    
    count = {word:1 for word in words}
    wordlength = len(words[0])
    res = []
    wordslength = len(words)*wordlength #the length of the combination we are looking for

    #we go till len(s)-wordslength, because after that it will be impossible to find a combination of the length we want
    #the remaining substring will be too short
    for left in range(len(s)-wordslength):

        #keep track of the words we have seen in the window
        wordsSeen = {}
        for right in range(len(words)):
            #this tells us where our word will start
            wordIndex = left+right * wordlength
            tempword = s[wordIndex:wordIndex+wordlength]

            if tempword not in count:
                break
            wordsSeen[tempword] = wordsSeen.get(tempword,0)+1

            if wordsSeen[tempword]>count[tempword]:
                break

        if wordsSeen == count:
            res.append(left)
    
    return res

findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"])