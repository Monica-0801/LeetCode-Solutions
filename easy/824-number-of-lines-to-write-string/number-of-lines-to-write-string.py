class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        l1 = 0
        c = 0
        for i in s:
            o = ord(i) - ord('a')
            if c + widths[o] <= 100:
                c += widths[o]
            else:
                c = widths[o]
                l1 += 1

        return [l1 + 1, c]