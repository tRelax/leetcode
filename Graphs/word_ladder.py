from typing import List
from collections import defaultdict, deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or beginWord == endWord:
            return 0

        neighbors = defaultdict(list)
        wordList.append(beginWord)

        # create a graph of all words that can be formed by changing one letter
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + '*' + word[i + 1:]
                neighbors[pattern].append(word)

        visit = set([beginWord])
        q = deque([(beginWord)])
        res = 1

        print(neighbors)

        # BFS
        while q:
            # for each word in the queue, check if it is the endWord
            for i in range(len(q)):
                word = q.popleft()
                # if the word is the endWord, return the result
                if word == endWord:
                    return res
                for i in range(len(word)):
                    pattern = word[:i] + '*' + word[i + 1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
            res += 1

        return 0


beginWord = "cat"
endWord = "sag"
wordList = ["bat", "bag", "sag", "dag", "dot"]

print(Solution().ladderLength(beginWord, endWord, wordList))  # 4
