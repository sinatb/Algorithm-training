class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        operators = ["*","/","+","-"]
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else:
                op2 = stack[-1]
                stack.pop()
                op1 = stack[-1]
                stack.pop()
                if t == "*":
                    stack.append(op1*op2)
                elif t == "/":
                    stack.append(op1//op2 if op1*op2 >= 0 else -(-op1//op2))
                elif t == "-":
                    stack.append(op1-op2)
                else:
                    stack.append(op1+op2)
        return stack[-1]