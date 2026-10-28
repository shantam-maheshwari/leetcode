from typing import List, Tuple

# # without caching (TLE)
# class Excel:
#     def __init__(self, height: int, width: str):
#         m = height
#         n = ord(width) - ord("A") + 1

#         self.mat = []
#         for i in range(m):
#             self.mat.append([])
#             for j in range(n):
#                 self.mat[i].append(TreeNode(0))

#     def set(self, row: int, column: str, val: int) -> None:
#         i, j = self.coords(row, column)
#         self.mat[i][j].val = val
#         self.mat[i][j].children = []

#     def get(self, row: int, column: str) -> int:
#         i, j = self.coords(row, column)
#         return self.mat[i][j].get()

#     def sum(self, row: int, column: str, numbers: List[str]) -> int:
#         i, j = self.coords(row, column)
#         self.mat[i][j].children = []

#         for number in numbers:
#             pairs = number.split(":")
#             if len(pairs) == 1:
#                 x, y = self.coords(int(pairs[0][1:]), pairs[0][0])
#                 self.mat[i][j].children.append(self.mat[x][y])
#             else:
#                 x1, y1 = self.coords(int(pairs[0][1:]), pairs[0][0])
#                 x2, y2 = self.coords(int(pairs[1][1:]), pairs[1][0])
#                 for x in range(x1, x2 + 1):
#                     for y in range(y1, y2 + 1):
#                         self.mat[i][j].children.append(self.mat[x][y])

#         return self.mat[i][j].get()

#     def coords(self, row: int, column: str) -> Tuple[int, int]:
#         return (row - 1, ord(column) - ord("A"))


# class TreeNode:
#     def __init__(self, val: int = 0):
#         self.val = val
#         self.children: List[TreeNode] = []

#     def get(self) -> int:
#         if not self.children:
#             return self.val

#         return sum([child.get() for child in self.children])


# with caching
class Excel:
    def __init__(self, height: int, width: str):
        m = height
        n = ord(width) - ord("A") + 1

        self.mat = []
        for i in range(m):
            self.mat.append([])
            for j in range(n):
                self.mat[i].append(TreeNode(0))

    def set(self, row: int, column: str, val: int) -> None:
        i, j = self.coords(row, column)
        self.mat[i][j].val = val
        self.mat[i][j].children = []
        self.mat[i][j].invalidate()

    def get(self, row: int, column: str) -> int:
        i, j = self.coords(row, column)
        return self.mat[i][j].get()

    def sum(self, row: int, column: str, numbers: List[str]) -> int:
        i, j = self.coords(row, column)
        self.mat[i][j].children = []
        self.mat[i][j].invalidate()

        for number in numbers:
            pairs = number.split(":")
            if len(pairs) == 1:
                x, y = self.coords(int(pairs[0][1:]), pairs[0][0])
                self.mat[i][j].children.append(self.mat[x][y])
                self.mat[x][y].parents.append(self.mat[i][j])
            else:
                x1, y1 = self.coords(int(pairs[0][1:]), pairs[0][0])
                x2, y2 = self.coords(int(pairs[1][1:]), pairs[1][0])
                for x in range(x1, x2 + 1):
                    for y in range(y1, y2 + 1):
                        self.mat[i][j].children.append(self.mat[x][y])
                        self.mat[x][y].parents.append(self.mat[i][j])

        return self.mat[i][j].get()

    def coords(self, row: int, column: str) -> Tuple[int, int]:
        return (row - 1, ord(column) - ord("A"))


class TreeNode:
    def __init__(self, val: int = 0):
        self.val = val
        self.children: List[TreeNode] = []
        self.valid = True
        self.parents: List[TreeNode] = []

    def get(self) -> int:
        if not self.children:
            return self.val

        if self.valid:
            return self.val

        self.val = 0
        for child in self.children:
            self.val += child.get()
        self.valid = True
        return self.val

    def invalidate(self):
        self.valid = False
        for parent in self.parents:
            parent.invalidate()


def test_Excel():
    e = Excel(3, "C")
    e.set(1, "A", 2)
    assert e.sum(3, "C", ["A1", "A1:B2"]) == 4
    e.set(2, "B", 2)
    assert e.get(3, "C") == 6
