class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ''.join(filter(str.isalnum, s)).lower()
        print(palindrome)
        return palindrome == palindrome[::-1]


sol = Solution()

ex = "0P"

print(sol.isPalindrome(ex))
