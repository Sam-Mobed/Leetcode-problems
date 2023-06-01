def isSubsequence(s, t):
    index=0
    
    for char in t:
        if char==s[index]:
            index+=1

    if (index==len(s)):
        return True
    
    return False

if __name__ == "__main__":
    t1 = "ahbgdc"
    s1 = "abc"
    print(isSubsequence(s1,t1))

    s2 = "axc"
    print(isSubsequence(s2,t1))