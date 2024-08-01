# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        left = head
        def get_middle(head):
            if head is None:
                return head
            slow = head
            fast = head

            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        def reverse_list(head):
            prev = None
            current = slow
            while current:
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev

        slow = get_middle(head)
        prev = reverse_list(slow)
        
        while left:
            if left.val != prev.val:
                return False
            prev = prev.next
            left = left.next
        return True

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

s = Solution()

s.isPalindrome(head)

