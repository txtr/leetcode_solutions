# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = l1
        node2 = l2
        
        carry = 0
        
        while not node1 is None:
            val1 = node1.val
            try:
                val2 = node2.val
            except AttributeError:
                val2 = 0
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            node1.val = digit
            
            if node1.next is None:
                if node2 is None:
                    if carry != 0:
                        node = ListNode(val = carry)
                        node1.next = node
                        carry = 0
                else:
                    if node2.next is None:
                        if carry != 0:
                            node = ListNode(val = carry)
                            node1.next = node
                            carry = 0
                    else:
                        node1.next = node2.next
                        node2.next = None

            node1 = node1.next
            if not node2 is None:
                node2 = node2.next
        return l1
            