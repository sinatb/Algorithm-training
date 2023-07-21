class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def backtrack(candidates,curr,answers,answer):
            if (curr < 0):
                return
            elif (curr == 0):
                answers.append(answer)
                return
            else:
                for c in candidates:
                    nans = answer[:]
                    nans.append(c)
                    backtrack(candidates,curr-c,answers,nans)
            return answers
        answers=[]
        answer=[]
        tmp = backtrack(candidates,target,answers,answer)
        frequencies = [Counter(lst) for lst in tmp]
        unique_frequencies = []
        for i in range(len(frequencies)):
            if frequencies[i] not in frequencies[i+1:]:
                unique_frequencies.append(tmp[i])
        return unique_frequencies