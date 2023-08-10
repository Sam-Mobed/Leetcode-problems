"""
Just to test stuff.
"""

def findKthLargest( nums, k: int) -> int:
        
        heap = []

        def heapify(h,index):
            if (2*index)+1<len(heap) and h[index]<h[(2*index)+1]:
                h[index], h[(2*index)+1] = h[(2*index)+1], h[index]
                heapify(h,(2*index)+1)
            if (2*index)+2<len(heap) and h[index]<h[(2*index)+2]:
                h[index], h[(2*index)+2] = h[(2*index)+2], h[index]
                heapify(h,(2*index)+2)

        for n in nums:
            heap.append(n)
            heapify(heap,0)
        
        for i in range(k):
            x = heap.pop()

        return x

findKthLargest([3,2,1,5,6,4],2)