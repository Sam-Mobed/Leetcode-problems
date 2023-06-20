
def removeElem(nums, val):
    notVal=0
    index=0
    while True:
        try:
            nums[index]
        except IndexError:
            break
        if(nums[index]==val):
            nums.pop(index)
        else:
            index+=1
            notVal+=1
    
    return notVal

if __name__=="__main__":
    test1=[3,2,2,3]
    val1=3
    sol1=removeElem(test1, val1)
    print(test1, sol1)

    test2=[0,1,2,2,3,0,4,2]
    val2=2
    sol2=removeElem(test2, val2)
    print(test2, sol2)