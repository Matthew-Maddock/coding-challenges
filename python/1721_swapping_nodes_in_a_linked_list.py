# 1721. Swapping Nodes in a Linked List - Medium

# You are given the head of a linked list, and an integer k.

# Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

# Example 1:

# Input: head = [1,2,3,4,5], k = 2
# Output: [1,4,3,2,5]
# Example 2:

# Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
# Output: [7,9,6,6,8,7,3,0,9,5]


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dictionary_ll = dict()
        i = 1
        temp = head
        while temp:
            dictionary_ll[i] = temp
            temp = temp.next
            dictionary_ll[i].next = None
            i += 1
        temp = dictionary_ll[k]
        dictionary_ll[k] = dictionary_ll[i - k]
        dictionary_ll[i - k] = temp
        new_head = dictionary_ll[1]
        new_head_return = new_head
        i = 2
        while i <= len(dictionary_ll):
            new_head.next = dictionary_ll[i]
            i += 1
            new_head = new_head.next
        return new_head_return
