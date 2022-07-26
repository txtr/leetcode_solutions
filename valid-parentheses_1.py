class Solution:
    def isValid(self, s: str) -> bool:
        stack  = []
        
        for x in s:
            try:
                if x == ')':
                    y = stack.pop(-1)
                    if not y == '(':
                        return False
                elif x == '}':
                    y = stack.pop(-1)
                    if not y == '{':
                        return False
                elif x == ']':
                    y = stack.pop(-1)
                    if not y == '[':
                        return False
                else:
                    stack.append(x)
            except IndexError:
                return False
        
        if not len(stack) == 0:
            return False
        return True
