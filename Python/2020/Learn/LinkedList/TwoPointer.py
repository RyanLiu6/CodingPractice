class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                print(slow.val)
                return True

        return False

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # O(n) time and space
        if not head:
            return None

        dict = {}

        while head:
            if dict.get(head, -1) == -1:
                dict[head] = 1
            else:
                return head

            head = head.next

        return None

        # O(n) time and O(1) space
        if not head:
            return None

        slow = head
        fast = head
        cycle = False

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                cycle = True
                break

        if cycle:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next

            return slow
        else:
            return None

    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        first = headA
        second = headB

        while first != second:
            if not first:
                first = headB
            else:
                first = first.next

            if not second:
                second = headA
            else:
                second = second.next

        return first
