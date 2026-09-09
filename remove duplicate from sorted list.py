'''

================================= Leet Code Problem ==========================

class Solution: 
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        res = head
        
        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return res 

================================= Leet Code Problem ============================

'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        res = head

        while head and head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next

        return res


# Create linked list:
# 1 → 1 → 2 → 3 → 3

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)

solution = Solution()
result = solution.deleteDuplicates(head)



while result:
    print(result.val, end=" → ")
    result = result.next

print("None")
    
