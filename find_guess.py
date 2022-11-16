# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        # using binary search method
        start = 1
        while start <= n:
            middle = (start + n) // 2
            g = guess(middle)
            
            if g == 0:
                return middle
            elif g == -1:
                n = middle - 1
            else:
                start = middle + 1