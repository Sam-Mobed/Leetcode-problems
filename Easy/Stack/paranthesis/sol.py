def isValid(s):
    pairs = {'{':'}','[':']','(':')'}
    stack=[]

    for paran in s:
        if len(stack)==0 or (paran in pairs.keys()):
            stack.append(paran)
        elif len(stack)==0 and (paran not in pairs):
            #dealing with a closing paranthesis that were never opened
            return False
        else:
            #we have a closing paranthesis
            #if it doesn't match with the last opening paran, then we return False
            key = stack[-1]
            closing = pairs[key]
            if closing!=paran:
                return False
            else:
                stack.pop()
    
    if len(stack)!=0:
        #in case we have a single opening paranthesis in s
        return False
    
    return True

isValid("}}")