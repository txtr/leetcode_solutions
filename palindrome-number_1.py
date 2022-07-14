class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            digits = []
            while x:
                digits.append(x % 10)
                x = x // 10

            print(digits)

            i = 0
            j = len(digits) - 1
            while i < j:

                print(i, j)

                if not digits[i] == digits[j]:
                    return False
                i = i + 1
                j = j - 1

            return True