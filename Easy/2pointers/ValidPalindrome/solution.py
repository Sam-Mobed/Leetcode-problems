
def isPalindrome(txt):
    #i'm sure there's a string method that puts everything to lowercase
    #and removes special characters, i;ll use it once i get internet again
    i=0
    j=len(txt)-1
    #have to break the loop once i is bigger than j
    while i<j:
        if(txt[i]!=txt[j]):
            return False
        i+=1
        j-=1

    return True



#for now we don't get rid of non-valid characters, gotta change that
if __name__ == "__main__":
    t1="amanaplanacanalpanama"
    print(isPalindrome(t1))

    t2="raceacar"
    print(isPalindrome(t2))

    t3=""
    print(isPalindrome(t3))
