class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if not stack:
                stack.append(s[i])
            else:
                if stack[-1] == s[i]:
                    stack.pop(-1)
                else:
                    stack.append(s[i])
        return "".join(stack)