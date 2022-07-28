class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        letters = []
        for x in s:
            if not x == '-':
                letters.append(x.upper())
        
        result = "".join(letters[0:(len(letters) % k)])
        del letters[0:(len(letters) % k)]
        
        while len(letters) > 0:
            if not result == "":
                result = result + "-"
            result = result + "".join(letters[0:k])
            del letters[0:k]
        return result
        