class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        st, fi = 1, max(piles)
        while st<fi:
            k = (st+fi)//2
            hp = sum(map(lambda x: ceil(float(x)/k),piles))
            if hp>h:
                st=k+1
            else:
                fi=k
        return st