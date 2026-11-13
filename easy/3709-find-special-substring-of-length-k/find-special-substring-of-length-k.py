class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        for i in range(len(s)-k+1):
            if len(set(s[i:i+k])) == 1:
                if i == 0:
                    if i+k == len(s) or s[i+k] != s[i]:
                        return True
                elif i+k == len(s):
                    if s[i-1] != s[i]:
                        return True
                else:
                    if s[i+k] != s[i] and s[i-1] != s[i]:
                        return True
        return False
