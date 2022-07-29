class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        result = []
        for word in words:
            flag = True
            
            bijection = {}
            domain = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
            
            for index, char in enumerate(word):
                try:
                    mapped = bijection[pattern[index]]
                except KeyError:
                    if char in domain:
                        bijection[pattern[index]] = char
                        domain.remove(char)
                        continue
                    else:
                        flag = False
                        break
                if not char == mapped:
                    flag = False
                    break
            if flag:
                result.append(word)
            print(bijection)
        return result
            