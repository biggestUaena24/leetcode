import re

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        while tokens:
            if re.match("[-+]?\d+$", tokens[0]):
                stack.append(int(tokens.pop(0)))
            else:
                b = stack.pop(-1)
                a = stack.pop(-1)

                if tokens[0] == "+":
                    stack.append(a + b)
                elif tokens[0] == "-":
                    stack.append(a - b)
                elif tokens[0] == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
                
                tokens.pop(0)
            
        return stack[-1]