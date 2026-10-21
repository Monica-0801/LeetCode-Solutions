class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        while len(stones) > 1:
            m1 = max(stones)
            stones.remove(m1)
            m2 = max(stones)
            stones.remove(m2)
            m = abs(m1 - m2)
            stones.append(m)
        return stones[0]