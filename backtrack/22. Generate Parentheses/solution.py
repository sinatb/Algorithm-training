class Solution(object):
    def backtrack(self,ans,s,n,stack):
        if (len(s) > 2*n):
            return
        elif len(s) == 2*n and len(stack) == 0:
            ans.append(s)
            return
        else:
            if (len(stack)==0 and len(s)!=2*n):
                stack.append("(")
                self.backtrack(ans,s+"(",n,stack)
            else:
                stack1 = stack[:]
                stack2 = stack[:]
                stack1.pop()                
                self.backtrack(ans,s+")",n,stack1)
                stack2.append("(")
                self.backtrack(ans,s+"(",n,stack2)
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        s=""
        ans=[]
        self.backtrack(ans,s,n,stack)
        return ans
