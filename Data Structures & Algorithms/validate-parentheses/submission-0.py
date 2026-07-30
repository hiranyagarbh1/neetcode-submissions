class Solution:
    def isValid(self, s: str) -> bool:

        prev_length = -1
        
        while len(s) != prev_length:
            prev_length = len(s)
            s = s.replace('()', '').replace('[]', '').replace('{}', '')
        return len(s) == 0


        