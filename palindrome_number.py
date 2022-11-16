#This is stringifying the number and this may not be efficient
class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        return string == string[::-1]