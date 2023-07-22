class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [0]
        ans = [0 for i in range(len(temperatures))]
        for i in range(1,len(temperatures)):
            while(stack and temperatures[i] > temperatures[stack[-1]]):
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans