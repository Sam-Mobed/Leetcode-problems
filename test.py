"""
Just to test stuff.
"""

def reverseVowels(s: str) -> str:

    vowels={'a','e','i','o','u','A','E','I','O','U'}
    s_arr = list(s)

    ptr1, ptr2 = 0, len(s_arr)-1

    while ptr1<ptr2:
        if s_arr[ptr1] not in vowels:
            ptr1+=1
            continue
        elif s_arr[ptr2] not in vowels:
            ptr2-=1
            continue
        
        s_arr[ptr1], s_arr[ptr2] = s_arr[ptr2], s_arr[ptr1]
        ptr1+=1
        ptr2-=1
    
    return ''.join(s_arr)


reverseVowels('hello')
