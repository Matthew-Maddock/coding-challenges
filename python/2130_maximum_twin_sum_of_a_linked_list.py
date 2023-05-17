# 2130. Maximum Twin Sum of a Linked List - Medium

# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

# Example 1:


# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6.

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(head: ListNode) -> ListNode:
            prev = None
            while head:
                next = head.next
                head.next = prev
                prev = head
                head = next
            return prev

        ans = 0
        slow = head
        fast = head

        # Let slow point to the start of the second half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Tail points to the end with reversed second half
        tail = reverseList(slow)

        while tail:
            ans = max(ans, head.val + tail.val)
            head = head.next
            tail = tail.next

        return ans
