class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        while s:
            try:
                letter = s[0:2]
            except:
                letter = s[0:1]
                
            print(letter, result)
            if letter == "IV":
                result = result + 4
                s = s[2:]
            elif letter == "IX":
                result = result + 9
                s = s[2:]
            elif letter == "XL":
                result = result + 40
                s = s[2:]
            elif letter == "XC":
                result = result + 90
                s = s[2:]
            elif letter == "CD":
                result = result + 400
                s = s[2:]
            elif letter == "CM":
                result = result + 900
                s = s[2:]
            elif letter[0] == "I":
                result =  result + 1
                s = s[1:]
            elif letter[0] == "V":
                result =  result + 5
                s = s[1:]
            elif letter[0] == "X":
                result =  result + 10
                s = s[1:]
            elif letter[0] == "L":
                result =  result + 50
                s = s[1:]
            elif letter[0] == "C":
                result =  result + 100
                s = s[1:]
            elif letter[0] == "D":
                result =  result + 500
                s = s[1:]
            elif letter[0] == "M":
                result =  result + 1000
                s = s[1:]
        return result
                