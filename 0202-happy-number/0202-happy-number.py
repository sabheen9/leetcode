class Solution:
    def isHappy(self, n: int) -> bool:
        n=str(n)
        num_set=[]
        result=0
        while result!=1:
            result=0
            for i in range(len(n)):
                result=result+pow(int(n[i]),2)
        
            if result in num_set:
                return False
        
            else:
                num_set.append(result)
        
            n=str(result)
            
        return True
    