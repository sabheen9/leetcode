class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s[::-1].lstrip()
        last_word=[]
        for i in range(len(s)):
            last_word.append(s[i])
            if (s[i]==' ') :
                last_word.pop()
                break
            elif len(s)==len(last_word):
                 break
        return len(last_word)