class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class ClassicSoln:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        curr = head
        retHead = ListNode(curr.val)
        curr = curr.next

        while curr:
            temp = ListNode(curr.val)
            temp.next = retHead
            retHead = temp

            curr = curr.next

        return retHead

    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head

        retHead = ListNode(-1)
        retHead.next = head
        prev = retHead

        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next

        return retHead.next

    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None

        first = head
        second = evenStart = first.next

        while first.next and second.next:
            first.next = first.next.next
            second.next = second.next.next

            first = first.next
            second = second.next

        first.next = evenStart

        return head
