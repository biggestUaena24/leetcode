class Solution:    
    def addBinary(self, a: str, b: str) -> str:
        # We should add from the last digit to the first digit
        # we do this by doing -1 - i in a for loop


        carry = 0
        solution = ""
        if len(a) > len(b):
            b = "0" * (len(a)-len(b)) + b
        elif len(b) > len(a):
            a = "0" * (len(b)-len(a)) + a

        for i in range(len(a)):
                if int(a[-1 - i]) + int(b[-1 - i]) + carry == 0:
                    carry = 0
                    solution = "0" + solution
                elif int(a[-1 - i]) + int(b[-1 - i]) + carry == 1:
                    carry = 0
                    solution = "1" + solution
                elif int(a[-1 - i]) + int(b[-1 - i]) + carry == 2:
                    carry = 1
                    solution = "0" + solution
                elif int(a[-1 - i]) + int(b[-1 - i]) + carry == 3:
                    carry = 1
                    solution = "1" + solution

        if carry == 1:
            return "1" + solution
        return solution

