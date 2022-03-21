class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListSolutions:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head or (n == 1 and not head.next):
            return None

        curr = head
        tempArr = []

        while curr is not None:
            tempArr.append(curr)
            curr = curr.next

        target = len(tempArr) - n
        if target == 0:
            return tempArr[1]
        else:
            tempArr[target - 1].next = tempArr[target].next

        return head

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

        while curr is not None:
            temp = ListNode(curr.val)
            temp.next = retHead
            retHead = temp
            curr = curr.next

        return retHead

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        [1,2,4]
        [1,3,4]
        """
        # Extra space
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

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        :input: 1->2
        :output: false
        """
        # O(n) time and space
        curr = head
        tempArr = []

        while curr is not None:
            tempArr.append(curr.val)
            curr = curr.next

        return (tempArr[::-1] == tempArr)

        # O(n) time and O(1) space
        if not head:
            return True

        length = 0
        curr = prev = head
        first = curr
        second = curr

        while curr is not None:
            length+=1
            curr = curr.next

        curr = head

        if length % 2 == 0:
            mid = length // 2
        else:
            mid = (length - 1) // 2

        for i in range(mid):
            prev = curr
            curr = curr.next

        prev.next = None
        if length % 2 == 0:
            second = curr
        else:
            second = curr.next

        first = self.reverseList(head)

        for i in range(mid):
            if first.val != second.val:
                return False

            first = first.next
            second = second.next

        return True
