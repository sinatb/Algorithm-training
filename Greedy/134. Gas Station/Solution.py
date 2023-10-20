class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        currgas = 0
        allgas = 0
        start = 0
        for i in range(len(gas)):
           currgas += gas[i] - cost[i] 
           allgas += gas[i] - cost[i]
           if (currgas < 0):
               start = i + 1
               currgas = 0
        if allgas < 0:
            return -1
        return start
