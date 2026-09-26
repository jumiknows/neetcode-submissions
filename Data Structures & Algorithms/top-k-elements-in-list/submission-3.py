class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      
        #[(3, 4), (2, 2)]
        top_items = Counter(nums).most_common(k)
    
        return [num for num, count in top_items]