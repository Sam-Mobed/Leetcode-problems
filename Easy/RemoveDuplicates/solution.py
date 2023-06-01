
def removeDups(nums):
    uniqueElems=len(nums)
    index=0
    previousElem=-200 #-200 cause restriction says nums cant contain int smaller than -100
    
    while True:
        try:
            nums[index]
        except IndexError:
            break
        if nums[index]==previousElem:
            nums.pop(index)
            uniqueElems-=1
            continue
        previousElem=nums[index]
        index+=1
    
    return uniqueElems


if __name__=="__main__":
    test1=[0,0,1,1,1,2,2,3,3,4]
    result1 = removeDups(test1)
    print(test1, result1)

    test2=[1,1,2]
    result2 = removeDups(test2)
    print(test2, result2)