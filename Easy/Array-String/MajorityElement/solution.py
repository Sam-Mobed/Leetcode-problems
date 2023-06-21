'''def findMajorityElem(nums):
    majorityThreshhold=len(nums)/2

    elements={}

    for num in nums:
        if str(num) not in elements:
            elements[str(num)]=1
        else:
            elements[str(num)]+=1
        
        if elements[str(num)]>majorityThreshhold:
            return num #should i output as string or int
        
    #assumption that there exists a majority element
    #but bad practice to not have return/exception statement outside loop (or is it ok?)
    raise Exception("Argument does not contain a majority element.")'''

def findMajorityElem(nums):
    nums.sort()

    majority=len(nums)/2

    counter=0
    currentElement='x'
    for elem in nums:
        if counter>majority:
            return currentElement

        if elem!=currentElement:
            currentElement=elem
            counter=1
        else:
            counter+=1

    return currentElement #we are guaranteed that the majority element exists though

if __name__=="__main__":
    test1=[3,3,4]
    print(findMajorityElem(test1))

    test2=[2,2,1,1,1,2,2]
    print(findMajorityElem(test2))