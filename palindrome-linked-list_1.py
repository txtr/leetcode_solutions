# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tail = head
        nodes = 1
        while not tail.next is None:
            next_node = tail.next
            next_node.prev = tail
            tail = next_node
            nodes = nodes + 1
        head.prev = None
        
        node_i = head
        node_j = tail
        while not node_i is node_j:
            if not node_i.val == node_j.val:
                return False
            node_i = node_i.next
            node_j = node_j.prev
        return True