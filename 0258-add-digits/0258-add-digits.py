class Solution:
    def addDigits(self, num: int) -> int:
        num=str(num)
        result=20
        while result>=10:
            result=0
            for i in range(len(num)):
                result=result+int(num[i])
        
            num=str(result)
        return num    