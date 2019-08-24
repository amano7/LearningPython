# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        l1: ListNode
        l2: ListNode
        """
        add = 0
        ans = []
        lis1 = []
        lis2 = []
        while l1:
            lis1.append(l1.val)
            l1 = l1.next
        while l2:
            lis2.append(l2.val)
            l2 = l2.next
        for i in range(len(lis1)):
            if len(lis1) > i:
                lis1[i] = 0
            if len(lis2) > i:
                lis2[i] = 0
            val = lis1[i] + lis2[i] + add
            if val > 9:
                add = 1
                ans.append(val - 10)
            else:
                add = 0
                ans.append(val)
        node = ListNode(ans[0])
        ret_node = node
        for i in range(1, len(ans)):
            node.next = ListNode(ans[i])
            node = node.next
        return ret_node


# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# if __name__ == "__main__":
#     s = Solution()
#     print(s.addTwoNumbers([2, 4, 3], [5, 6, 4]))
