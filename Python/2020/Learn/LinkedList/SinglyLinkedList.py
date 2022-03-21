class SinglyNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:
            return -1

        curr = self.head

        for i in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        newHead = SinglyNode(val)
        newHead.next = self.head
        self.head = newHead

        if self.size == 0:
            self.tail = newHead

        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        if self.size == 0:
            self.addAtHead(val)
            return

        tail = SinglyNode(val)
        self.tail.next = tail
        self.tail = tail

        self.size += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == self.size:
            self.addAtTail(val)
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index < 0 or index > self.size:
            return

        curr = self.head
        insertNode = SinglyNode(val)

        for i in range(index - 1):
            curr = curr.next

        insertNode.next = curr.next
        curr.next = insertNode
        self.size += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return
        if index == 0:
            head = head.next
            self.size -= 1
            return

        curr = self.head

        for i in range(index - 1):
            curr = curr.next

        curr.next = curr.next.next
        if index == self.size - 1:
            self.tail = curr

        self.size -= 1
