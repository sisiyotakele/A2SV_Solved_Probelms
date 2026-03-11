class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                st = ''
                while stack and stack[-1] != "[":
                    st = stack.pop() + st
                stack.pop()

                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num

                stack.append(int(num) * st)
        return "".join(stack)
