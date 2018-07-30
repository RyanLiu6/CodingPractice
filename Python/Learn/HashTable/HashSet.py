import time

class HashSetSolution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        mySet = set(nums)

        if len(mySet) != len(nums):
            return True
        else:
            return False

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # With extra space
        nDict = {}
        for num in nums:
            curr = nDict.get(num, -1)
            if curr == -1:
                nDict[num] = 1
            else:
                nDict[num] = curr + 1

        for num in nums:
            if nDict[num] == 1:
                return num

        # No extra space
        result = 0

        for num in nums:
            result^=num

        return result

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        if not nums1 or not nums2:
            return result

        set1 = set(nums1)
        for num in nums2:
            if num in set1:
                result.append(num)
                set1.remove(num)

        return result

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = 0
        numSet = set()
        strNum = str(n)

        while result != 1:
            result = 0
            for num in strNum:
                curr = int(num)*int(num)
                result += curr
            if result in numSet:
                return False
            strNum = str(result)
            numSet.add(result)

        return True
