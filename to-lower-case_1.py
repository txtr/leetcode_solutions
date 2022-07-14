class Solution:
    def toLowerCase(self, s: str) -> str:
        mapp= {
                "A":"a",
                "B":"b",
                "C":"c",
                "D":"d",
                "E":"e",
                "F":"f",
                "G":"g",
                "H":"h",
                "I":"i",
                "J":"j",
                "K":"k",
                "L":"l",
                "M":"m",
                "N":"n",
                "O":"o",
                "P":"p",
                "Q":"q",
                "R":"r",
                "S":"s",
                "T":"t",
                "U":"u",
                "V":"v",
                "W":"w",
                "X":"x",
                "Y":"y",
                "Z":"z"
        }
        
        result = ""
        i = 0
        while True:
            try:
                letter = s[i]
            except IndexError:
                break
            try:
                result = result + mapp[letter]
            except KeyError:
                result = result + letter
            i = i + 1
        return result
            