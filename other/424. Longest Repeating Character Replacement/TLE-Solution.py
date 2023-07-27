class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        print(len(s))
        l = k + 2
        ans = l-1
        prev_ans = 0
        for i in range(l,len(s)+1):
            if (prev_ans == ans):
                return ans
            prev_ans = ans
            ctr = Counter(s[0:i])
            x = ctr.values()
            x.sort(reverse=True)
            if (k>=sum(x[1:])):
                ans = i
                continue
            for j in range(len(s)-i):
                ctr[s[j]]-=1
                if (j+i<len(s) and ctr[s[j+i]]):
                    ctr[s[j+i]] += 1
                elif (j+i<len(s) and not ctr[s[j+i]]):
                    ctr[s[j+i]] = 1
                x = ctr.values()
                x.sort(reverse=True)
                if (k>=sum(x[1:])):
                    ans = i
                    break
        return ans