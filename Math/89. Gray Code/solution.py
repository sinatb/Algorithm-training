class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        base_list = [0,1]
        for i in range(n-1):
            r = []
            for j in range(len(base_list)):
                r.append(base_list[j]+ 2**(i+1))
            r.reverse()
            base_list+=r
        print(base_list)
        return base_list