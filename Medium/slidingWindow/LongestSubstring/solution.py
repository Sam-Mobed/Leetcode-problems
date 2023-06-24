def findLongestSubstring(s):
    longest=""
    currentString=""

    for char in s:
        try:
            if(char in currentString):
                if(len(currentString)>len(longest)):
                    longest=currentString

                currentString=""
        except IndexError:
            currentString+=char #we have this try catch block for when currentString is empty
            continue

        currentString+=char

    return len(longest)

if __name__=="__main__":
    s1="abcabcbb"
    print(findLongestSubstring(s1))

    s2="bbbbb"
    print(findLongestSubstring(s2))

    s3="pwwkew"
    print(findLongestSubstring(s3))