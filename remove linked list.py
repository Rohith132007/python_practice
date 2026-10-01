'''

======================================= Leet Code Problem ========================================

class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0)
        ans.next = head
        ans = dummy
        
        while dummy is not None:
            while dummy.next is not None and dummy.next.val == val:
                dummy.next = dummy.next.next
            dummy = dummy.next
        return ans.next
        
========================================= Test Cases =========================================

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):

        ans = ListNode(0)
        ans.next = head
        dummy = ans

        while dummy is not None:

            while dummy.next is not None and dummy.next.val == val:
                dummy.next = dummy.next.next

            dummy = dummy.next

        return ans.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(6)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(6)
head.next.next.next.next.next.next = ListNode(4)

val = 6

solution = Solution()
result = solution.removeElements(head, val)

current = result

while current is not None:
    print(current.val, end=" → ")
    current = current.next

print("None")