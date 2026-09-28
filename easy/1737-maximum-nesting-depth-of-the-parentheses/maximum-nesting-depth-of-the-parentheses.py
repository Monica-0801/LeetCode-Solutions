class Solution:
    def maxDepth(self, s: str) -> int:
        m = 0
        c = 0
        for i in s:
            if i == '(':
               c += 1
               m = max(c,m)
            elif i == ')':
                c -= 1
        return m