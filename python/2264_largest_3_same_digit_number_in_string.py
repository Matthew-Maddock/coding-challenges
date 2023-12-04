# 2264. Largest 3-Same-Digit Number in String - Easy

# You are given a string num representing a large integer. An integer is good if it meets the following conditions:

# It is a substring of num with length 3.
# It consists of only one unique digit.
# Return the maximum good integer as a string or an empty string "" if no such integer exists.

# Note:

# A substring is a contiguous sequence of characters within a string.
# There may be leading zeroes in num or a good integer.


# Example 1:

# Input: num = "6777133339"
# Output: "777"
# Explanation: There are two distinct good integers: "777" and "333".
# "777" is the largest, so we return "777".
# Example 2:


# Input: num = "2300019"
# Output: "000"
# Explanation: "000" is the only good integer.


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # Initialize max_num to -1, to track the largest triplet
        max_num = -1

        # Set the left pointer to the start of the string
        l = 0

        # Set the right pointer next to the left pointer
        r = 1

        # Iterate as long as the right pointer is within the string
        while r < len(num):
            # If current characters at left and right pointers are different
            if num[l] != num[r]:
                # Move left pointer to the right pointer's position
                l = r

                # Increment the right pointer
                r += 1

            # If current characters at left and right pointers are the same
            else:
                # If a triplet is formed
                if r - l == 2:
                    # Update max_num with the largest digit among the found triplets
                    max_num = max(max_num, int(num[l]))

                    # Move left pointer to the position after the current triplet
                    l = r + 1

                    # Reset right pointer to one position after the new left pointer
                    r = l + 1

                else:
                    # If a triplet is not formed yet, increment the right pointer
                    r += 1

        # Return an empty string if no triplet is found, otherwise return the largest triplet
        return "" if max_num == -1 else f"{max_num}" * 3
