

def mergeArrays(nums1, nums2, m, n):
    if m==0:
        #nums1=nums2 this doesn't work, because you are creating a new pointer to nums2, but the original list pointed to by nusm1 doesn't change, and that is exactly what the solution is looking at. The judge doesn't follow the pointer, it looks at the original place in the memory where nums1 was located
        del nums1 [:]
        nums1+=nums2
        return
    if n==0:
        return

    #remember, n and m represent the actual length, not the index.
    n-=1
    m-=1
    while n>-1:
        if (nums2[n]>=nums1[m]):
            nums1.pop() #pop the last element first so there is less to shift
            nums1.insert(m+1, nums2[n])
            n-=1
        elif (m!=0):
            m-=1
        else:
            #nums1=nums2[:n+1]+nums1 we get the result but this creates a new list instead of storing inside nums1
            for i in range(n, -1, -1):
                nums1.insert(0, nums2[i])
                nums1.pop()
            break

#tests
#it works but we have to get rid of the 0's at the end of nums1
if __name__=="__main__":
    test1=[2,0]
    nums12=[1]
    mergeArrays(test1, nums12, 1, 1)
    print(test1) #[1,2,2,3,5,6]

    test2=[1]
    nums22=[]
    mergeArrays(test2, nums22, 1, 0)
    print(test2) #[1]

    test3=[0]
    nums32=[1]
    mergeArrays(test3, nums32, 0, 1)
    print(test3) #[1]