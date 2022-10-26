class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        for i in s[::-1].strip():
            if i.isalpha():
                k +=1
            else:
                break
        return k

