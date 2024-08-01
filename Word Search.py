from typing import List


# incomplete
def exist(board: List[List[str]], word: str) -> bool:
    a = 0

    def dfs(i, j, k=0):
        if k == len(word):
            return True
        if (
            i < 0
            or j < 0
            or i >= len(board)
            or j >= len(board[0])
            or board[i][j] != word[k]
        ):
            return False
        temp, board[i][j] = board[i][j], "/"
        found = (
            dfs(i + 1, j, k + 1)
            or dfs(i - 1, j, k + 1)
            or dfs(i, j + 1, k + 1)
            or dfs(i, j - 1, k + 1)
        )
        board[i][j] = temp

    while a < len(word):
        for i, k in enumerate(board):
            for j, m in enumerate(k):
                if dfs(i, j):
                    return True

        a += 1


a = exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED")
print(a)
