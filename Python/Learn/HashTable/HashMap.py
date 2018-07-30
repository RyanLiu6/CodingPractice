class HashMapSolution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resDict = {}
        for i in range(len(nums)):
            resDict[nums[i]] = i

        for i in range(len(nums)):
            req = target - nums[i]
            first = i

            if resDict.get(req, -1) is not -1 and first is not resDict[req]:
                return (i, resDict[req])

    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(set(s)) != len(set(t)):
            return False

        charMap = {}

        for i in range(len(s)):
            key = s[i]
            val = t[i]
            if not key in charMap:
                charMap[key] = val
            elif charMap[key] != val:
                return False

        return True

    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        retList = []
        if not list1 or not list2:
            return retList

        dict1 = {}
        dict2 = {}
        n = len(list1)
        m = len(list2)
        shortest = n + m

        for i in range(n):
            dict1[list1[i]] = i

        for i in range(m):
            dict2[list2[i]] = i

        for key, value in dict1.items():
            if key in dict2:
                curr = dict2[key] + value
                if curr < shortest:
                    shortest = curr
                    retList.clear()
                    retList.append(key)
                elif curr == shortest:
                    retList.append(key)

        return retList

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        freqMap = [0 for _ in range(26)]
        n = len(s)
        shift = ord("a")

        for i in range(n):
            key = s[i]
            freqMap[ord(key) - shift] += 1

        for i in range(n):
            key = s[i]
            if freqMap[ord(key) - shift] == 1:
                return i

        return -1

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        retList = []
        if not nums1 or not nums2:
            return retList

        freqMap = {}

        for num in nums1:
            if num in freqMap:
                freqMap[num] += 1
            else:
                freqMap[num] = 1

        for num in nums2:
            if num in freqMap and freqMap[num] > 0:
                retList.append(num)
                freqMap[num] -= 1

        return retList

    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numDict = {}

        for key, val in enumerate(nums):
            if not val in numDict:
                numDict[val] = key
            else:
                if abs(numDict[val] - key) <= k:
                    return True
                numDict[val] = key

        return False
