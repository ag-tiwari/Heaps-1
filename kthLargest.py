'''
TC: O(n log k) 
where in n is the length of array that we have to iterate and k is the size of min heap
SC: O(k) where k is the size of minHeap

Approach we could have created a max heap and popped k times to return our output but that is not
efficient because we have to create a heap of size O(n) in that case and in the tc would go O(nlogn).

Therefore to optimize it we create a min heap which would limit our size to O(k) and TC to O(nlogk)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        heapq.heapify(minHeap)
        for num in nums:
            heapq.heappush(minHeap,num)
            if len(minHeap)>k:
                minHeap.heapq.heappop()
        
        return minheap[0]