from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        w1=Counter(words1)
        w2=Counter(words2)  
        c=0
        for i in w1:
            if w1[i] == 1:
                if i in words2:
                    if w2[i] == 1:
                        c += 1
        return c