import random


class Solution:
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.baseList = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.baseList

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        retArr = self.baseList.copy()
        for i in range(len(retArr)):
            newPos = random.randint(0, i)
            retArr[i], retArr[newPos] = retArr[newPos], retArr[i]

        return retArr

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if len(self.minStack) == 0 or x < self.getMin():
            self.minStack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        

    def top(self):
        """
        :rtype: int
        """

    def getMin(self):
        """
        :rtype: int
        """

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
