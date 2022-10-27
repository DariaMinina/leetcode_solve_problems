import math


class Solution:
    def line_reflection(self, points):
        minX = math.inf
        maxX = -math.inf
        seen = set()

        for x, y in points:
            minX = min(minX, x)
            maxX = max(maxX, x)
            seen.add((x, y))

        sumX = maxX + minX

        return all((sumX - x, y) in seen for x, y in points)


if __name__ == "__main__":
    sol = Solution()
    points = [[1, 1], [-1, 1]]
    print(sol.line_reflection(points))

