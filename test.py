"""
Just to test stuff.
"""

def threeSum(nums):
    triplets=[]
    nums.sort()
    left,right=0,len(nums)-1

    while True:
        if left==right:
            break
        if abs(nums[left])>nums[right]:
            left+=1
        else:
            right-=1
        for i in range(left+1,right):
            s = nums[left]+nums[i]+nums[right]
            if s==0 and ([nums[left],nums[i],nums[right]] not in triplets):
                triplets.append([nums[left],nums[i],nums[right]])

    return triplets

threeSum([0,0,0])