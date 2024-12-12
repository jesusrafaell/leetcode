# 23. Merge k Sorted Lists


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in lists:
            head = i
            while head:
                arr.append(head.val)
                head = head.next

        arr.sort()
        ans = curr = ListNode()
        for n in arr:
            n = ListNode(n)
            curr.next = n
            curr = n

        return ans.next
