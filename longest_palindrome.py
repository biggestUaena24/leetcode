# This is the solution that is using O(n ** 2) since it is checking every substring in the string to return the max substring of the solution list
def isPalindrome(s: str) -> str:
    return s == s[::-1]

def longestPalindrome(s: str) -> str:
    solution = ""
    for i in range(len(s)):
        for j in range(i, len(s)):
            if isPalindrome(s[i:j+1]):
                if len(s[i:j+1]) > len(solution):
                    solution = s[i:j+1]
    
    return solution

# This is the solution that we use check if a string is palindrome from the center of the substring to get the biggest substring
def longestPalindrome_2(self, s: str) -> str:
    res = ""
    reslen = 0

    for i in range(len(s)):
        #for the odd length
        l , r = i , i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l : r + 1]
                reslen = r - l  + 1
            l -= 1
            r += 1
        
        l , r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > reslen:
                res = s[l : r + 1]
                reslen = r - l  + 1
            l -= 1
            r += 1
    
    return res

print(longestPalindrome("abcdefggfedcba"))