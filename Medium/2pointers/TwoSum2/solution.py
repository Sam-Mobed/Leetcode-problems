

#the fact is they're sorted
#have to be wise in how we choose our pointers
#say pointer1 points to beginning of array (so smallest number)
#target-pointer1
"""
if the target is negative, then we have to look at the beginning of array

so index1<index2

the below solution has a time complexity of O(n^2) using brute force.
think of a solution that has a smaller time complexity.
"""

def twoSum(numbers, target):
    index1=0
    while index1<len(numbers):
        index2=index1+1
        while index2<len(numbers):
            if (numbers[index1]+numbers[index2]==target):
                return [index1+1,index2+1]
            index2+=1
        index1+=1
    
    raise Exception("There must be a solution, but none was found")

if __name__=="__main__":
    nums1=[2,7,11,15]
    target1=9
    print(twoSum(nums1,target1))

    nums2=[2,3,4]
    target2=6
    print(twoSum(nums2,target2))

    nums3=[-1,0]
    target3=-1
    print(twoSum(nums3,target3))