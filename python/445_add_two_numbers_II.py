# 445. Add Two Numbers II - Medium

# You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: l1 = [7,2,4,3], l2 = [5,6,4]
# Output: [7,8,0,7]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1)
            l1 = l1.next

        while l2:
            stack2.append(l2)
            l2 = l2.next

        head = None
        carry = 0

        while carry or stack1 or stack2:
            if stack1:
                carry += stack1.pop().val
            if stack2:
                carry += stack2.pop().val
            node = ListNode(carry % 10)
            node.next = head
            head = node
            carry //= 10

        return head
