from collections import defaultdict

class Solution:

    #valid 
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        word_dict = {}
        for word in strs:
            alphabet = [0] * 26
            used_letters = list(word)
            for u in used_letters:
                alphabet[ord(u) - 97] += 1
            if str(alphabet) in word_dict:
                word_dict[str(alphabet)].append(word)
            else:
                word_dict[str(alphabet)] = [word]

        solution = []
        for anagrams in word_dict.values():
            solution.append(anagrams)
        return solution
    
    #better

    def groupAnagramsBetter(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)

        return(list(res.values()))

sol = Solution()

strs = ["act","pots","tops","cat","stop","hat"]
sol.groupAnagrams(strs)
sol.groupAnagramsBetter(strs)
