class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        mid = len(s) // 2
        count1 = 0
        count2 = 0
        s1 = s[:mid]
        s2 = s[mid :]

        for i in range(mid):
            if s1[i] in vowel:
                count1 += 1
            if s2[i] in vowel:
                count2 += 1

        return count1 == count2