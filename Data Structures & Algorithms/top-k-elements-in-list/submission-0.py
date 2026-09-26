class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. defaultdict(int) is faster than count.get(num, 0)
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            
        # 2. Create the empty buckets
        freq = [[] for _ in range(len(nums) + 1)]
        
        # 3. Group numbers by frequency
        for num, c in count.items():
            freq[c].append(num)
            
        # 4. The Optimized Extraction (Early Exit)
        res = []
        # Iterate backwards from the highest possible frequency down to 1
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # The exact moment we hit k elements, stop everything and return!
                if len(res) == k:
                    return res