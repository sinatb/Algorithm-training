class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmp = defaultdict(str)
        for s in strs:
            if (tmp[str(sorted(s))]):
                tmp[str(sorted(s))].append(s)
            else:
                tmp[str(sorted(s))] = [s]
        print(tmp)
        return tmp.values()