import pytest


class Solution:
    # # ugly
    # def simplifyPath(self, path: str) -> str:
    #     path += "/"
    #     stack = ["/"]

    #     for c in path:
    #         if c == ".":
    #             if stack[-1] == "/":
    #                 stack.append(c)
    #             else:
    #                 stack[-1] += c
    #         elif c == "/":
    #             if stack[-1] == "/":
    #                 continue
    #             elif stack[-1] == ".":
    #                 stack.pop()  # remove .
    #             elif stack[-1] == "..":
    #                 stack.pop()  # remove ..
    #                 if len(stack) > 1:
    #                     stack.pop()  # remove /
    #                     stack.pop()  # remove dir
    #             else:
    #                 stack.append(c)
    #         elif stack[-1] == "/":
    #             stack.append(c)
    #         else:
    #             stack[-1] += c

    #     # remove trailing /
    #     if len(stack) > 1 and stack[-1] == "/":
    #         stack.pop()

    #     return "".join(stack)

    # elegant
    def simplifyPath(self, path: str) -> str:
        stack = []
        print(path.split("/"))

        for token in path.split("/"):
            if token == "." or token == "":
                continue
            elif token == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return "/" + "/".join(stack)


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
    ],
)
def test_simplifyPath(path: str, expected: str):
    assert Solution().simplifyPath(path) == expected
