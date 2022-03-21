from SinglyLinkedList import *
from ClassicProb import *
from Conclusion import *

# ll = MyLinkedList()
#
# ll.addAtHead(7)
# ll.addAtHead(2)
# ll.addAtHead(1)
# ll.addAtIndex(3,0)
# ll.deleteAtIndex(2)
# ll.addAtHead(6)
# ll.addAtTail(4)
# ll.addAtHead(4)
# ll.addAtIndex(5,0)
# ll.addAtHead(6)

# ll.addAtHead(1)
# ll.addAtTail(3)
# ll.addAtIndex(1,2)

soln = ConcluSoln()

test = ListNode(1)
test.next = ListNode(2)
test.next.next = ListNode(3)
test.next.next.next = ListNode(4)
test.next.next.next.next = ListNode(5)
test.next.next.next.next.next = ListNode(6)
test.next.next.next.next.next.next = ListNode(7)
test.next.next.next.next.next.next.next = ListNode(8)

retNode = soln.rotateRight(test, 3)

print("_________________________________")
while retNode:
    print(retNode.val)
    retNode = retNode.next
