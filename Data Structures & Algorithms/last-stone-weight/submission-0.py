class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()  # Sorts ascending, so the two heaviest are at the end
            y = stones.pop()  # Heaviest stone
            x = stones.pop()  # Second heaviest stone
            
            if x != y:
                stones.append(y - x)  # Push the remaining weight back
                
        return stones[0] if stones else 0