# 69. Sqrt(x) - Easy

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 2:
            return x

        start = 0
        end = x / 2

        while start <= end:

            mid = int((start + end) / 2)

            square = mid * mid

            if square == x:
                return mid

            if square > x:
                end = mid - 1

            else:
                start = mid + 1

        return int(end)
