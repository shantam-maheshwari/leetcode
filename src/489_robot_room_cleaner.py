# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        steps = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def backtrack(i: int, j: int, direction: int):
            robot.clean()
            visited.add((i, j))

            for _ in range(4):
                if robot.move():
                    # update coordinates
                    i1 = i + steps[direction][0]
                    j1 = j + steps[direction][1]

                    if (i1, j1) not in visited:
                        backtrack(i1, j1, direction)

                    # return
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()

                # turn to the next direction
                direction = (direction + 1) % 4
                robot.turnRight()

        backtrack(0, 0, 0)
