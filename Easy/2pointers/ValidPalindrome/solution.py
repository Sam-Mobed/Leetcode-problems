
def isPalindrome(s: str) -> bool:

    if len(s)<2:
        return True
    
    pointer1=0
    pointer2=len(s)-1

    while pointer1<pointer2:
        if (not s[pointer1].isalnum()) and (type(s[pointer1])!=int):
            pointer1+=1
            continue
        elif (not s[pointer2].isalnum()) and (type(s[pointer1])!=int):
            pointer2+=1
            continue
        print(s[pointer1], s[pointer2])
        if type(s[pointer1])!=type(s[pointer2]):
            return False
        elif type(s[pointer1])==int and s[pointer1]!=s[pointer2]:
            return False
        elif s[pointer1].lower()!=s[pointer2].lower():
            return False
        
        pointer1+=1
        pointer2-=1
    
    return True



#for now we don't get rid of non-valid characters, gotta change that
if __name__ == "__main__":
    t1="A man, a plan, a canal: Panama"
    print(isPalindrome(t1))

    t2="raceacar"
    print(isPalindrome(t2))

    t3=""
    print(isPalindrome(t3))
