# 839. Similar String Groups - Hard

# Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

# For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

# Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

# We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

# Example 1:

# Input: strs = ["tars","rats","arts","star"]
# Output: 2
# Example 2:

# Input: strs = ["omv","ovm"]
# Output: 1

from typing import List


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        n, l = len(strs), len(strs[0])
        p = list(range(n))
        for i in range(n):
            for j in range(i + 1, n):
                if sum(strs[i][k] != strs[j][k] for k in range(l)) <= 2:
                    p[find(i)] = find(j)
        return sum(i == find(i) for i in range(n))
