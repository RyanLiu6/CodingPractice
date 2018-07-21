class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class ConcluSoln:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        retHead = prev = curr = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                curr.val = l1.val
                l1 = l1.next
            else:
                curr.val = l2.val
                l2 = l2.next

            curr.next = ListNode(0)
            prev = curr
            curr = curr.next

        if l1:
            prev.next = l1
        else:
            prev.next = l2

        return retHead

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        retNode = currNode = ListNode(0)
        currVal = 0

        while l1 or l2 or currVal:
            if l1:
                currVal += l1.val
                l1 = l1.next
            if l2:
                currVal += l2.val
                l2 = l2.next

            currNode.next = ListNode(currVal % 10)
            currNode = currNode.next
            currVal//=10

        return retNode.next

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return
        
        curr = head
        length = 1

        while curr.next:
            length += 1
            curr = curr.next

        curr.next = head
        k = k % length

        if k != 0:
            # do shit
            for i in range(length - k):
                curr = curr.next

        retHead = curr.next
        curr.next = None

        return retHead
