import heapq
import random
from datetime import datetime

class ConcluSolution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        count = 0
        if not J or not S:
            return 0

        myDict = {}
        for i in range(len(J)):
            myDict[J[i]] = i

        count = 0

        for s in S:
            if myDict.get(s, -1) != -1:
                count += 1

        return count

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
        Input:
        A = [ 1, 2]
        B = [-2,-1]
        C = [-1, 2]
        D = [ 0, 2]

        Output:
        2

        1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
        2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
        """

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        :input: [1,1,1,2,2,3], k = 2
        :output: [1,2]
        """
        freqMap = {}
        for num in nums:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        maxHeap = []
        for key, value in freqMap.items():
            maxHeap.append((-value, key))

        heapq.heapify(maxHeap)

        retList = []
        for _ in range(k):
            retList.append(heapq.heappop(maxHeap)[1])

        return retList

class RandomizedSet:
    """
    Operations must be average O(1)
    insert(val): Inserts an item val to the set if not already present.
    remove(val): Removes an item val from the set if present.
    getRandom: Returns a random element from current set of elements.
    Each element must have the same probability of being returned.
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nDict = {}
        self.nums = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nDict:
            return False
        else:
            self.nums.append(val)
            self.nDict[val] = len(self.nums) - 1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nDict:
            index = self.nDict[val]
            replace = self.nums[-1]
            self.nums[index], self.nDict[replace] = replace, index
            self.nums.pop()
            self.nDict.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
