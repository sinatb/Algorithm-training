class Solution(object):
    numbers = {
        '2' : ["a","b","c"],
        '3' : ["d","e","f"],
        '4' : ["g","h","i"],
        '5' : ["j","k","l"],
        '6' : ["m","n","o"],
        '7' : ["p","q","r","s"],
        '8' : ["t","u","v"],
        '9' : ["w","x","y","z"],
    }
    def backtrack(self,digits,str,answers):
        if (len(str) == len(digits)):
            if (len(digits) != 0):
                answers.append(str)
        else:
            for c in self.numbers[digits[len(str)]]:
                str2 = str+c
                self.backtrack(digits,str2,answers) 
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        answers = []
        self.backtrack(digits,"",answers)
        return answers
