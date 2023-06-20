'''
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
'''
def removeDups(nums):
    limit=len(nums)

    #the only corner case with this soluton
    if limit<2:
        return

    newElement=1
    counter=1
    for index in range(limit):
        try:
            while nums[index]==nums[newElement]:
                newElement+=1
        except IndexError:
            break

        '''if newElement-index==1:
            newElement+=1
            continue
        else:'''
        nums[index+1]=nums[newElement]
        counter+=1

    return counter


if __name__=="__main__":
    #test1=[1,2]
    test1=[0,0,1,1,1,2,2,3,3,4]
    result1 = removeDups(test1)
    print(test1, result1)


    test1=[0,0,1,1,1,2,2,3,3,4]
    result1 = removeDups(test1)
    print(test1, result1)

    test2=[1,1,2]
    result2 = removeDups(test2)
    print(test2, result2)