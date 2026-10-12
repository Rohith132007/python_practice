'''

=============================== Leet Code Problem ===============================

class Solution:
    def isPalindrome(self, head) -> bool:
        values = []

        current = head

        while current:
            values.append(current.val)
            current = current.next

        return values == values[::-1]

================================= Test Cases =================================

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head) -> bool:
        values = []

        current = head

        while current:
            values.append(current.val)
            current = current.next

        return values == values[::-1]


# Create linked list: 1 → 2 → 2 → 1
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)

solution = Solution()

print(solution.isPalindrome(head))