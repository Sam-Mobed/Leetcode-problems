
def removeElem(nums, val):
    notVal=0
    index=0
    while True:
        try:
            nums[index]
        except IndexError:
            break
        if(nums[index]==notVal):
            nums.pop(index)
            continue
        index+=1
        notVal+=1
    
    return notVal