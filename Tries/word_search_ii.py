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
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for w in words:
            root.addWord(w)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or (r, c) in visit
                    or board[r][c] not in node.children):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            # up
            dfs(r + 1, c, node, word)
            # down
            dfs(r - 1, c, node, word)
            # right
            dfs(r, c + 1, node, word)
            # left
            dfs(r, c - 1, node, word)

            visit.remove((r, c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        return list(res)


board = [
    ["a", "b", "c", "d"],
    ["s", "a", "a", "t"],
    ["a", "c", "k", "e"],
    ["a", "c", "d", "n"]
]
words = ["bat", "cat", "back", "backend", "stack"]
print(Solution().findWords(board, words))  # ["cat","back","backend"]
