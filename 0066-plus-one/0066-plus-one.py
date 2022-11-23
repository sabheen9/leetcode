class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list1=[]
        new_string="".join([str(n) for n in digits])
        string_ans=str((int(new_string) + 1))

        for n in string_ans:
             list1.append(int(n))
        return list1