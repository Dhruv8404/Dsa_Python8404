class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def getIntersectionNode(self, headA_list, headB_list):
        def list_to_linked_list(lst):
            if not lst:
                return None
            head = ListNode(lst[0])
            current = head
            for val in lst[1:]:
                current.next = ListNode(val)
                current = current.next
            return head

        headA = list_to_linked_list(headA_list)
        headB = list_to_linked_list(headB_list)

        temp = headA
        while temp and headB:
            if temp.next is None:
                temp.next = headB
            if headB.next is None:
                headB.next = headA
            if headB.next.val == temp.next.val:
                return temp.val
            temp = temp.next

# Given data in lists
headA_list = [4, 1, 8, 4, 5]
headB_list = [5, 6, 1, 8, 4, 5]

# Create an instance of Solution
solution = Solution()
result = solution.getIntersectionNode(headA_list, headB_list)
print(result)
