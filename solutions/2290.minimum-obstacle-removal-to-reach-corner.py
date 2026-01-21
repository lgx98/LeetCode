#
# @lc app=leetcode id=2290 lang=python3
#
# [2290] Minimum Obstacle Removal to Reach Corner
#


# @lc code=start
from collections.abc import Generator
from typing import NamedTuple

Point = NamedTuple("Point", [("x", int), ("y", int)])


class Solution:
    WIDTH: int
    HEIGHT: int

    def _neighbors(self, p: Point) -> Generator[Point, None, None]:
        if p.x > 0:  # west
            yield Point(p.x - 1, p.y)
        if p.y > 0:  # north
            yield Point(p.x, p.y - 1)
        if p.x < self.WIDTH - 1:  # east
            yield Point(p.x + 1, p.y)
        if p.y < self.HEIGHT - 1:  # south
            yield Point(p.x, p.y + 1)

    def minimumObstacles(self, grid: list[list[int]]) -> int:
        self.WIDTH = len(grid[0])
        self.HEIGHT = len(grid)
        epoch: int = -1  # = -(obstacles_removed + 1)
        grid[0][0] = epoch
        grid[self.HEIGHT - 1][self.WIDTH - 1] = 2
        to_visit: list[Point] = [Point(0, 0)]

        while True:
            next_epoch = epoch - 1
            visit_next = []
            while to_visit:
                cell = to_visit.pop()
                for n in self._neighbors(cell):
                    match grid[n.y][n.x]:
                        case val if val < 0:
                            pass
                        case 2:  # reached destination
                            return -epoch - 1
                        case 1:
                            visit_next.append(n)
                            grid[n.y][n.x] = next_epoch
                        case 0:
                            to_visit.append(n)
                            grid[n.y][n.x] = epoch
                        case _:
                            assert False
            epoch = next_epoch
            to_visit = visit_next

# @lc code=end
if __name__ == "__main__":
    grid = [[0,1,0,0,0],[1,1,1,1,1],[0,0,0,1,0]]
    s = Solution()
    print(s.minimumObstacles(grid))
    for row in grid:
        print(row)
