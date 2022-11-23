import math
class Solution:
    def mySqrt(self, x: int) -> int:
        

        if x<=0:
            x=x*(-1)
        sqrt_num=math.floor(math.sqrt(x))
        return sqrt_num