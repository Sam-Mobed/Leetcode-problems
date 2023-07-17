"""
Just to test stuff.
"""

def evalRPN(tokens) -> int:
        
    #the last value that computed
    operations = {"+", "-", "*", "/"}
    
    #at the end there will be a single value in the stack, and it will be the result
    tokensStack=[]

    for token in tokens:
        if token not in operations:
            tokensStack.append(int(token))
        else:
            #the order matters
            num2=tokensStack.pop()
            num1=tokensStack.pop()
            if token=="+":
                tokensStack.append(num1+num2)
            elif token=="-":
                tokensStack.append(num1-num2)
            elif token=="*":
                tokensStack.append(num1*num2)
            else:
                tokensStack.append(num1//num2)

    return tokensStack[0]

evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])