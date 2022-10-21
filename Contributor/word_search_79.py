def exist(self, board, word):
        def backtrack(word, i, j, m, n):
            if board[i][j] != word[self.l]:
                return
            visited.add((i, j))
            self.l += 1
            if self.l == len(word):
                self.is_found = True
                return 
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                i1, j1 = i + di, j + dj
                if 0 <= i1 < m and 0 <= j1 < n and (i1, j1) not in visited:
                    backtrack(word, i1, j1, m, n)
                    if self.is_found:
                        return 
            visited.remove((i, j))
            self.l -= 1
        
        if not board or not board[0]:
            return False
        if word == '':
            return True
        m, n = len(board), len(board[0])
        self.is_found = False
        self.l = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                backtrack(word, i, j, m, n)
                if self.is_found:
                    return True
        return False
