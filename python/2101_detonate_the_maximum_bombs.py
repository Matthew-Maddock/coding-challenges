# 2101. Detonate the Maximum Bombs - Medium

# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.

# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.

# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.

# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

# Example 1:

# Input: bombs = [[2,1,3],[6,1,4]]
# Output: 2
# Explanation:
# The above figure shows the positions and ranges of the 2 bombs.
# If we detonate the left bomb, the right bomb will not be affected.
# But if we detonate the right bomb, both bombs will be detonated.
# So the maximum bombs that can be detonated is max(1, 2) = 2.
from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs) -> int:
        adj, m = defaultdict(list), len(bombs)

        def canDetonate(b1, b2):
            x1, y1, r1 = b1
            x2, y2, r2 = b2
            return (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1**2

        for i in range(m):
            for j in range(m):
                if i == j:
                    continue
                if canDetonate(bombs[i], bombs[j]):
                    adj[i].append(j)

        def dfs(node, seen):
            seen.add(node)
            for nei in adj[node]:
                if nei not in seen:
                    dfs(nei, seen)

        ctr = 0

        for idx, bomb in enumerate(bombs):
            seen = set()
            dfs(idx, seen)
            ctr = max(ctr, len(seen))

        return ctr
