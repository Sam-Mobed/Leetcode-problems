#i'm thinking greedy algorithm here, find the max, pop it
#and add it's value to the localsum until we reach goal. shouldn't 
#be harder

#the greedy approach is going to have a bigger time complexity
#to optimize we would probably have to use dynamic programming

def minSubArray(nums ,target):
    subArray=[]
    while(nums!=[]):
        maxNum = nums.pop(nums.index(max(nums)))
        subArray.append(maxNum)
        if (sum(subArray)>=target):
            return len(subArray)
    return 0


if __name__=="__main__":
    nums1=[2,3,1,2,4,3]
    print(minSubArray(nums1, 7))

    nums2=[1,4,4]
    print(minSubArray(nums2, 4))

    nums3=[1,1,1,1,1,1,1,1]
    print(minSubArray(nums3, 11))