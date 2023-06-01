

def mergeArrays(nums1, nums2, m, n):
    i=0
    j=0
    if(n==0):
        return
    if(m==0):
        nums1.clear()
        nums1+=nums2
        #nums1=nums2 can't change the identity of mutable obj inside of a function
        return
    while j<n:
        while(nums1[i]<nums2[j]):
            i+=1
            if (i==len(nums1)):
                #here we have to clear all the remaining 0's inside
                #nums1
                nums1+=nums2 #we've gone through nums1
                return
        nums1.insert(i, nums2[j])
        nums2.pop(j)
        j+=1

#tests
#it works but we have to get rid of the 0's at the end of nums1
if __name__=="__main__":
    test1=[1,2,3,0,0,0]
    nums12=[2,5,6]
    mergeArrays(test1, nums12, 3, 3)
    print(test1) #[1,2,2,3,5,6]

    test2=[1]
    nums22=[]
    mergeArrays(test2, nums22, 1, 0)
    print(test2) #[1]

    test3=[0]
    nums32=[1]
    mergeArrays(test3, nums32, 0, 1)
    print(test3) #[1]