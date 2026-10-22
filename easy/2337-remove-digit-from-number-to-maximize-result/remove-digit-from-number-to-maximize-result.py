class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l = []
        for i in range(len(number)):
            if number[i] == digit:
                l.append(i)
        for i in range(len(l)):
            a = l[i]
            l[i] = int(number[:a] + number[a + 1:])
        return str(max(l))