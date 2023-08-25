"""
Just to test stuff.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchMatrix(matrix,target) -> bool:

    if not matrix or not matrix[0]:
        return False
    
    

    def findRow(row1,row2):
        #get the mid row
        #if the first element of the mid row is bigger, then check first of matrix
        #if the first element of the mid row is smaller, check the second second half od the matrix
        #this will always return the row where the target is supposed to be.
        if row1>row2:
            return -1
        mid = (row1+row2)//2
        l = matrix[mid][0]
        r = matrix[mid][-1]
        if l<=target<=r:
            return mid
        elif target<l:
            return findRow(row1,mid-1)
        else:
            return findRow(mid+1,row2)

    def binarySearch(l,r,row):
        #normal binary search
        if l>r:
            return False
        m = (l+r)//2
        if matrix[row][m]>target:
            return binarySearch(l,m-1,row)
        elif matrix[row][m]<target:
            return binarySearch(m+1,r,row)
        else:
            return True
    
    row = findRow(0,len(matrix)-1)
    return binarySearch(0,len(matrix[row])-1,row)


searchMatrix([[1]],2)