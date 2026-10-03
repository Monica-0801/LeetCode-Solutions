class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        l = [0,0]
        for i in events:
            if i == 'W':
                l[1] += 1
            elif i == 'WD' or i == 'NB':
                l[0] += 1
            else:
                l[0] += int(i)
                
            if l[1] == 10:
                return l
        return l