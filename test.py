"""
Just to test stuff.
"""

def superDigit(n, k):
    
    def recursive(num):
        if len(num)==1:
            return int(num)
        result=0
        for digit in num:
            result+=int(digit)
        return recursive(str(result))
    
    return recursive(n)


superDigit('9875',4)
