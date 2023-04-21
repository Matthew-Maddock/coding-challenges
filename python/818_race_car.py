# 818. Race Car - Hard

# Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

# When you get an instruction 'A', your car does the following:
# position += speed
# speed *= 2
# When you get an instruction 'R', your car does the following:
# If your speed is positive then speed = -1
# otherwise speed = 1
# Your position stays the same.
# For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

# Given a target position target, return the length of the shortest sequence of instructions to get there.

# Example 1:

# Input: target = 3
# Output: 2
# Explanation:
# The shortest instruction sequence is "AA".
# Your position goes from 0 --> 1 --> 3.


class Solution:
    def racecar(self, target: int) -> int:
        def bfs():
            from collections import deque

            Q = deque([(0, 1, 0)])
            seen = {(0, 1)}
            if target == 0:
                return 0
            while True:
                p, s, d = Q.popleft()
                if p == target:
                    return d
                for action in [True, False]:
                    if action:
                        this_p = p + s
                        s *= 2
                        if this_p == target:
                            return d + 1
                        if (this_p, s) not in seen:
                            seen.add((this_p, s))
                            Q.append((this_p, s, d + 1))
                    else:
                        if s > 0:
                            s = -1
                        else:
                            s = 1
                        if (p, s) not in seen:
                            seen.add((p, s))
                            Q.append((p, s, d + 1))

        return bfs()
