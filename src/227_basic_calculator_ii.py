import pytest

# class Solution:
#     def calculate(self, s: str) -> int:
#         sign = "+"
#         operand = 0
#         stack = []

#         for i, c in enumerate(s):
#             if c.isdigit():
#                 operand = operand * 10 + int(c)

#             if not (c.isdigit() or c == " ") or i == len(s) - 1:
#                 if sign == "+":
#                     stack.append(operand)
#                 elif sign == "-":
#                     stack.append(-operand)
#                 elif sign == "*":
#                     stack.append(stack.pop() * operand)
#                 elif sign == "/":
#                     stack.append(int(stack.pop() / operand))

#                 sign = c
#                 operand = 0

#         return sum(stack)


# same solution as above, more intuitive implementation
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        last_operator = "+"

        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = 0
                j = i
                while j < len(s) and s[j].isdigit():
                    num = num * 10 + int(s[j])
                    j += 1

                if last_operator == "+":
                    stack.append(num)
                elif last_operator == "-":
                    stack.append(-num)
                elif last_operator == "*":
                    stack.append(stack.pop() * num)
                elif last_operator == "/":
                    stack.append(int(stack.pop() / num))

                i = j
                continue

            if s[i] in ["+", "-", "*", "/"]:
                last_operator = s[i]
                i += 1
                continue

            i += 1

        return sum(stack)


@pytest.mark.parametrize(
    ("s", "expected"), [("3+2*2", 7), (" 3/2 ", 1), ("14-3/2", 13)]
)
def test_calculate(s: str, expected: int):
    assert Solution().calculate(s) == expected
