def rotateArray(nums, k):
    while(k!=0):
        num = nums.pop()
        nums.insert(0, num)
        k-=1


if __name__=="__main__":
    nums1 = [1,2,3,4,5,6,7]
    rotateArray(nums1,3)
    print(nums1)

    nums2 = [-1,-100,3,99]
    rotateArray(nums2,2)
    print(nums2)

