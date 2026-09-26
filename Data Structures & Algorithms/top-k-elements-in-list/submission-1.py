class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
# Counter(nums) counts everything automatically.
        # .most_common(k) grabs the top k results as pairs like: [(3, 4), (2, 2)]
        top_items = Counter(nums).most_common(k)
        
        # Pull just the numbers out of those pairs
        return [num for num, count in top_items]