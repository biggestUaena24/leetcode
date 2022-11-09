class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        reslen = 0
        checked = []

        for i in range(len(s)):
            index = i
            templen = 0
            checked.clear()

            while index < len(s):
                if s[index] not in checked:
                    checked.append(s[index])
                    templen += 1
                else:
                    break
                
                index += 1

            if templen > reslen:
                reslen = templen
            

        return reslen
