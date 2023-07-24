class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def backtrack(visited,m,n,k):
            visited[m][n]=1
            if (k == len(word)):
                return True
            b = False
            if (m<len(board)-1 and visited[m+1][n] == 0 and board[m+1][n] == word[k]):
                nv = copy.deepcopy(visited)
                b = backtrack(nv,m+1,n,k+1)
            if (not b and n<len(board[0])-1 and visited[m][n+1] == 0 and board[m][n+1] == word[k]):
                nv = copy.deepcopy(visited)
                b = backtrack(nv,m,n+1,k+1)
            if (not b and n>0 and visited[m][n-1] == 0 and board[m][n-1] == word[k]):
                nv = copy.deepcopy(visited)
                b = backtrack(nv,m,n-1,k+1)
            if (not b and m>0 and visited[m-1][n] == 0 and board[m-1][n] == word[k]):
                nv = copy.deepcopy(visited)
                b = backtrack(nv,m-1,n,k+1)
            return b
        
        word_count = Counter(word)
        board_count = Counter(''.join([''.join(row) for row in board])) 
        for char in word:
            if word_count[char] > board_count[char]:
                return False
    
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]

        for i in range(len(board)):
            for j in range(len(board[0])):
                visited =[[0 for m in range(len(board[0]))] for n in range(len(board))]
                if (board[i][j] == word[0] and backtrack(visited,i,j,1)):
                    return True
        return False
        