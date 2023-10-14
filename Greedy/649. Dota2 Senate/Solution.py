class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        l_senate = list(senate)
        d_ctr = senate.count('D')
        r_ctr = senate.count('R')
        rb = db = 0
        for i in l_senate:
            if (rb == r_ctr):
                return 'Dire'
            elif (db == d_ctr):
                return 'Radiant'
            if (i == 'R'):
                if (rb > 0):
                    rb -= 1
                else:
                    l_senate.append('R')
                    db += 1
            else:
                if (db > 0):
                    db -= 1
                else:
                    l_senate.append('D')
                    rb += 1
    