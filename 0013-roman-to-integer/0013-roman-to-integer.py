class Solution:
    def romanToInt(self, s: str) -> int:
        sum=0		
        roman_number=dict(I=1,V=5,X=10,L=50,C=100,D=500,M=1000)

        s = s.replace('IV', 'IIII') \
             .replace('IX', 'VIIII') \
             .replace('XL', 'XXXX') \
             .replace('XC', 'LXXXX') \
             .replace('CD', 'CCCC') \
             .replace('CM', 'DCCCC')
             
        for i in range(len(s)):
            if s[i] in roman_number.keys():       
                sum=sum+roman_number.get(s[i])
        return sum

