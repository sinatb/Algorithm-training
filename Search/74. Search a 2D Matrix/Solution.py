class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        rows = len(matrix)
        columns = len(matrix[0])
        l = 0
        r = rows*columns - 1
        while (l <= r):
            mid = (l+r)//2
            tmid = matrix[mid//columns][mid%columns]
            if (tmid > target):
                r = mid - 1
            elif (tmid < target):
                l = mid + 1
            else:
                return True
        return False