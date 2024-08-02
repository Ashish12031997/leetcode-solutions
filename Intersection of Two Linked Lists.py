from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:

    # reverse both linkedin list
    def reverse_list(head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev

    rev_headA = reverse_list(headA)
    rev_headB = reverse_list(headB)

    while rev_headA and rev_headB:
        if rev_headA.val != rev_headB.val:
            print(rev_headA.val)
        rev_headA = rev_headA.next
        rev_headB = rev_headB.next
    return True

head = ListNode(4)
head.next = ListNode(1)
head.next.next = ListNode(8)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head2 = ListNode(5)
head2.next = ListNode(6)
head2.next.next = ListNode(1)
head2.next.next.next = ListNode(8)
head2.next.next.next.next = ListNode(4)
head2.next.next.next.next.next = ListNode(5)
print(getIntersectionNode(head,head2 ))
