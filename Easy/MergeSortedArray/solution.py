#two sorted arrays in increasing order
#merge the two array

#loop through array1 (by index), for each of its elements check if the corresponding
#one in arr2 is bigger, if it is, insert it.

#if element in array2 is bigger, we don't increment the counter


#is it good practice to modify the argument and return it?
#don't think so, but here the result should not be returned but instead
#stored inside arr1, so its fine

#the accomodation where len(arr1)=m+n changes things a lot

#in python(like many other OOP languages, the only mode of parameter
#passing is call by sharing. this  means thaat the parameters inside the 
#function become aliases of fthe actual arguments
#so function can change mutable objects passed as arguments,
#but can't change their identity

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
    while (j<n):
        if (nums1[i]>=nums2[j]):
            nums1.insert(i, nums2[j]) 
            j+=1
            i+=1
            continue
        i+=1
        if(i==n):
            break

#tests
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