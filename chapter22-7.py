# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        l3 = []
        while l1:
            l3.append(l1.val)
            l1 = l1.next
        while l2:
            l3.append(l2.val)
            l2 = l2.next
        l3.sort()
        res = ListNode(l3[0])
        return res
if __name__ == "__main__":
    s = Solution()
    print(s.mergeTwoLists([1, 2, 4], [1, 3, 4]))

