class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0 
        for i,v in enumerate(s):
            reversed_value = 26 - (ord(v) - ord('a'))
            position = i+1
            total += reversed_value * position

        return total