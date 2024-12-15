from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        cur = self

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isWord = True


class Solution:
    # using Trie
    def exist(self, board: List[List[str]], word: str) -> bool:
        root = TrieNode()
        root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                (r, c) in visited or
                    board[r][c] not in node.children):
                return
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                return True
            res = (dfs(r - 1, c, node, word) or
                   dfs(r + 1, c, node, word) or
                   dfs(r, c - 1, node, word) or
                   dfs(r, c + 1, node, word))

            visited.remove((r, c))
            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, root, ""):
                    return True
        return False

    def exist2(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs(r, c, i):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                    (r, c) in visited):
                return False

            visited.add((r, c))
            res = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )
            visited.remove((r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False


board = [
    ["A", "B", "C", "D"],
    ["S", "A", "A", "T"],
    ["A", "C", "A", "E"]
]
word = "CAT"

Solution().exist(board, word)

board = [
    ["A", "B", "C", "D"],
    ["S", "A", "A", "T"],
    ["A", "C", "A", "E"]
]
word = "BAT"
Solution().exist(board, word)
