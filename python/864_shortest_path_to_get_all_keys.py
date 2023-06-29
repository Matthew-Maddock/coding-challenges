# 864. Shortest Path to Get All Keys - Hard

# You are given an m x n grid grid where:

# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
# You start at the starting point and one move consists of walking one space in one of the four cardinal directions. You cannot walk outside the grid, or walk into a wall.

# If you walk over a key, you can pick it up and you cannot walk over a lock unless you have its corresponding key.

# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter of the first k letters of the English alphabet in the grid. This means that there is exactly one key for each lock, and one lock for each key; and also that the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

# Return the lowest number of moves to acquire all keys. If it is impossible, return -1.

# Example 1:

# Input: grid = ["@.a..","###.#","b.A.B"]
# Output: 8
# Explanation: Note that the goal is to obtain all the keys not to open all the locks.
import collections
from typing import List


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        keys = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "@":
                    start = (i, j)
                elif grid[i][j].islower():
                    keys += 1
        q = collections.deque()
        q.append((start[0], start[1], 0))
        visited = set()
        visited.add((start[0], start[1], 0))
        steps = 0
        while q:
            for _ in range(len(q)):
                row, col, key = q.popleft()
                if grid[row][col].islower():
                    key |= 1 << (ord(grid[row][col]) - ord("a"))
                if key == (1 << keys) - 1:
                    return steps
                for r, c in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] != "#":
                        if grid[r][c].isupper() and key & (1 << (ord(grid[r][c]) - ord("A"))) == 0:
                            continue
                        if (r, c, key) not in visited:
                            q.append((r, c, key))
                            visited.add((r, c, key))
            steps += 1
        return -1
