class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        rev = x[::-1]
        if x == rev:
            return True
        else:
            return False