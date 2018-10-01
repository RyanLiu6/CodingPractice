def moveZeroes(nums):
    if not nums:
        return

    nonZero = 0
    n = len(nums)

    for i in range(n):
        if nums[i] != 0:
            nums[nonZero], nums[i] = nums[i], nums[nonZero]
            nonZero+=1

def jag_phone_1(dominos):
    # 1. Use a dictionary with tuple as key
    # 2. Use first number * 10 + second number
    print("hello")

# distinct subsequences
def jag_phone_2(s, t):
    # S is base
    # T is target
    retArr = []

    DSHelper(retArr, s, t, "", 0)

    return len(retArr)

def DSHelper(retArr, string, target, prefix, index):
    print(prefix)
    if prefix == target:
        retArr.append(prefix)

    for i in range(index, len(string)):
        DSHelper(retArr, string, target, prefix + string[i], i + 1)

    """
    1. If target = "cat", create array of size 3 for subsequences
    index 0 is for seeing the subsequence c
    index 1 is for seeing the subsequence ca
    index 2 is for seeing the subsequence cat

    index 1 = index 1 + index 0
    index 2 = index 2 + index 1
    index 3 = index 3 + index 2

    and return index 3
    """

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

def minMeetingRoomsII(intervals):
    """
    :type intervals: List[Interval]
    :rtype: int
    """
    # Sort by Start Time
    intervals.sort(key=lambda x:x[0])
    heap = []
    heapq.heappush(heap, intervals[0][1])

    for i in range(1, len(intervals)):
        if intervals[i].start > heap[0]:
            heapq.heapreplace(heap, intervals[i][1])
        else:
            heapq.heappush(heap, intervals[i][1])

    return len(heap)

test = [[0, 30],[5, 10],[15, 20]]
minMeetingRoomsII(test)

class Graph:
    def __init__(self, ID):
        self.children = []
        self.ID = ID

    def addChild(self, child):
        self.children.append(child)

def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """
    if not prerequisites:
        return True

    gDict = {}

    # Sort by Parent (Assume each prereq is a pair)
    prerequisites.sort(key=lambda x:x[0])

    for cl in prerequisites:
        parent = cl[0]
        curr = Graph(cl[0])

        if parent in gDict:
            curr = gDict[parent]
        else:
            gDict[parent] = curr

        curr.addChild(cl[1])
