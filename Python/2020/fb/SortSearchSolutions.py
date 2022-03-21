class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        queue = []

        dummy = ListNode(0)
        curr = dummy

        for node in lists:
            heapq.heappush(queue, (node.val, node))

        while queue:
            node = heapq.heappop(queue)
            curr.next = node[1]
            curr = curr.next

            if curr.next:
                heapq.heappush(queue, (curr.val, curr.next))

        return dummy.next
