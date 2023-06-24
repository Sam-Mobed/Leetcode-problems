def containsNearbyDuplicate(nums, k) -> bool:

    #we need to keep track of indices too
    d = {}

    for index, num in enumerate(nums):
        
        d[num] = index #we don't care if it existed before, we keep the most recent index
        i = d[num]
        #indices.append(index)

        if i!=index and nums[i]==nums[index] and abs(i-index)<=k:
            return True

    return False

containsNearbyDuplicate([1,2,3,1], 3)

"""
The values of the dictionary are lists, and you're attempting to modify these lists directly. However, in Python, lists are mutable objects, and when you assign a list to a variable, you are actually assigning a reference to that list. As a result, when you append to indices, you're modifying the original list that was assigned to it, which affects all subsequent iterations.

To fix this, you can create a new list each time you need to append to indices. 


"""

d={}
d.get(1,[])
print(d)