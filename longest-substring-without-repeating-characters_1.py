class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_occurence = {}
        table = [0]
        for end in range(len(s)):
            try:
                table.append(min(end - last_occurence[s[end]], table[-1] + 1))
            except KeyError:
                try:
                    table.append(table[-1] + 1)
                except IndexError:
                    table.append(1)
            last_occurence[s[end]] = end
        return max(table)