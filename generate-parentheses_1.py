class Solution:
    result = []
    
    def generate(self, s: str, n: int, opened: int = 0, closed : int = 0):
        if opened == n and closed == n:
            self.result.append(s)
        else:
            if opened < n:
                self.generate(s = (s + '('), n = n, opened = opened + 1, closed = closed)
            if not opened - closed == 0:
                    self.generate(s = (s + ')'), n = n, opened = opened, closed = closed + 1)
    
    def generateParenthesis(self, n: int) -> List[str]:
        self.generate(s = "", n = n)
        return self.result