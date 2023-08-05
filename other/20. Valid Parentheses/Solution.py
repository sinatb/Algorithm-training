class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                elif c == ')' and stack[-1] != "(":
                    return False
                elif c == '}' and stack[-1] != "{":
                    return False
                elif c == ']' and stack[-1] != "[":
                    return False
                stack.pop()
        if len(stack) != 0:
            return False
        return True