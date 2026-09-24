class Solution:
    def numberOfPairs(self, nums: list[int]) -> list[int]:
        n = Counter(nums)
        output = [0,0]
        for i in n:
            if n[i] % 2 == 0:
                output[0] += n[i] // 2
            else:
                output[0] += (n[i] - 1) // 2
                output[1] += 1
        return output