"""
Just to test stuff.
"""

def canJump(nums) -> bool:

        skip=0

        for index, jumpVal in enumerate(nums):
            if skip!=0:
                skip-=1
                continue
            #this is as far as you can go
            nextIndex = index + jumpVal

            if nextIndex>=len(nums)-1 and nums[-1]-jumpVal<=1:
                return True
            
            #next we find the highest but achievable step that we can reach.
            maxVal=0
            maxValIndex=0
            if nextIndex>len(nums)-1:
                nextIndex = len(nums)-1

            while nextIndex!=index:
                if nums[nextIndex]>maxVal and nums[nextIndex]-jumpVal<=1:
                    maxVal = nums[nextIndex]
                    maxValIndex = nextIndex
            
                nextIndex-=1

            skip = (maxValIndex - index) -1
            
        return False


canJump([2,3,1,1,4])